from datetime import datetime

from flask import jsonify, request
from flask.views import MethodView

from .db_mongo import DbMongo


class ItemView(MethodView):
    def __init__(self, collect, query, filter_keys, *args, **kwargs):
        self.collect = collect
        self.query = query
        self.filter_keys = filter_keys
        self.client = DbMongo()

    def get_params(self, request):
        skip = request.args.get("skip", 0)
        limit = request.args.get('limit', 10)
        return int(skip), int(limit)

    def get(self):
        skip, limit = self.get_params(request)
        start_time = datetime.timestamp(datetime.utcnow())
        collects = self.client.find_all_from_collect(self.collect, query=self.query, filter_keys=self.filter_keys,
                                                     skip=skip,
                                                     limit=limit)
        end_time = datetime.timestamp(datetime.utcnow())
        return jsonify({
            self.collect: collects,
            "time": end_time - start_time
        })


class JobItemView(ItemView):
    def __init__(self, *args, **kwargs):
        self.collect = "jobs"
        self.query = {}
        self.filter_keys = ("_id",)
        super(JobItemView, self).__init__(self.collect, self.query, self.filter_keys, *args, **kwargs)


class CompanyItemView(ItemView):
    def __init__(self, *args, **kwargs):
        self.collect = "company"
        self.query = {}
        self.filter_keys = ("_id",)
        super(CompanyItemView, self).__init__(self.collect, self.query, self.filter_keys, *args, **kwargs)


class RelationItemView(ItemView):
    def __init__(self, *args, **kwargs):
        self.collect = "relation"
        self.query = {}
        self.filter_keys = ("_id", "job_id", "company_id")
        super(RelationItemView, self).__init__(self.collect, self.query, self.filter_keys, *args, **kwargs)

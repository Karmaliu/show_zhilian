from pymongo import MongoClient

from .config import MONGO_SERVER


class DbMongo():

    def __init__(self, mongo_server=MONGO_SERVER):
        db_client = MongoClient("mongodb://{user}:{pwd}@{host}:{port}/{db}".format(**mongo_server))
        db_name = mongo_server["db"]
        self.db = db_client[db_name]

    def find_all_from_collect(self, collect_name, query=None, filter_keys=("_id",), limit=10):
        if not query:
            query = {}
        filter_dict = {key: False for key in filter_keys}
        items = self.db[collect_name].find(query, filter_dict).limit(limit)
        rsp = [item for item in items]
        return rsp

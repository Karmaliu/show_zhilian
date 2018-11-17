from datetime import datetime

from flask import jsonify, url_for, render_template

from src.zhilian import zhilian_app
from .db_mongo import DbMongo


@zhilian_app.route('/test', methods=["POST", "GET"])
def db():
    start_time = datetime.timestamp(datetime.utcnow())
    client = DbMongo()
    jobs = client.find_all_from_collect("jobs")
    companys = client.find_all_from_collect("company")
    relations = client.find_all_from_collect("relation", filter_keys=("_id", "job_id", "company_id"))
    end_time = datetime.timestamp(datetime.utcnow())
    return jsonify(
        {"jobs": jobs, "companys": companys, "relations": relations, "time": end_time - start_time})


@zhilian_app.route("/", methods=["GET"])
def index():
    urls = [
        url_for("admin_app.index"),
        url_for("zhilian_app.db")
    ]
    return render_template("index.html", urls=urls)
    # return jsonify({"urls": urls})

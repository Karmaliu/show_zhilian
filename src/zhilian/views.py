from src.zhilian import zhilian_app


@zhilian_app.route("/", methods=["GET", "POST"])
def index():
    return "zhilian_app.index"
    # client = MongoClient()
    # jobs = client.find_all_by_collection("company")
    # return jsonify(jobs)

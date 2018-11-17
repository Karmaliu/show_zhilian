from pymongo import MongoClient

MONGO_SERVER = {
    "host": "server.asppj.top",
    "port": 27017,
    "db": "zhilian",
    "user": "zhilian_db",
    "pwd": "zhilian_db123"
}


class DbMongo():

    def __init__(self, mongo_server=MONGO_SERVER):
        db_client = MongoClient("mongodb://{user}:{pwd}@{host}:{port}/{db}".format(**mongo_server))
        db_name = MONGO_SERVER["db"]
        self.db = db_client[db_name]

    def find_all_from_collect(self, collect_name, filter_keys=("_id",), limit=100):
        filter_dict = {key: False for key in filter_keys}
        items = self.db[collect_name].find({}, filter_dict).limit(limit)
        rsp = [item for item in items]
        return rsp

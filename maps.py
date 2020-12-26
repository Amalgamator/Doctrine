from pymongo import MongoClient


dbclient = MongoClient('localhost', 27017)
db = dbclient.doctrine


def generate_mappool():
    mappool = {}
    for doc in db.mappool.find():
        map = {}
        for k, v in doc.items():
            if k == "_id":
                pass
            else:
                map[k] = v
        mappool.append(map)
    return mappool

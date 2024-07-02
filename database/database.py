import pymongo


def get_scene(id_: int, *, db: dict = None) -> dict:
    if not dict:
        raise ValueError("db must be provided")

    with pymongo.MongoClient(db["url"]) as client:
        collection = client[db["db"]]["Scenes"]
        return collection.find_one({"id": id_})

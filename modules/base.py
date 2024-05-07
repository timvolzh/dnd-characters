from pymongo import MongoClient

MONGO_ADDRESS = 'localhost:27017'
MONGO_USER = 'root'
MONGO_PASSWORD = 'example'

MONGO_DB_NAME = 'article'
MONGO_COLLECTION_USER = 'user'
MONGO_COLLECTION_CHAR = 'char'




class MongoDB(object):
    def __init__(self, host: str = MONGO_ADDRESS,
                 port: int = 27017,
                 db_name: str = MONGO_DB_NAME,
                 collection: str = MONGO_COLLECTION_USER):
        self._client = MongoClient(f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{host}/')
        self._collection = self._client[db_name][collection]

    def create_user(self, user: dict):
        try:
            if self._collection.find_one({"username": user.get('username')}) is None:
                self._collection.insert_one(user)
                print(f"Added New user: {user.get('username')}")
            else:
                print(f"User: {user.get('username')} in collection")
        except Exception as ex:
            print("[create_user] Some problem...")
            print(ex)

    def get_all_users(self):
        try:
            data = self._collection.find()
            for post in self._collection.find():
                print(post)
            print("Get all users")
            return data
        except Exception as ex:
            print("[get_all] Some problem...")
            print(ex)

    def find_by_username(self, username: str):
        try:
            data = self._collection.find_one({"username": username})
            print("Get user by username")
            return data
        except Exception as ex:
            print("[find_by_username] Some problem...")
            print(ex)

    def change_user(self, username: str, key: str, value: str):
        try:
            if self._collection.find_one({"username": username}) is not None:
                # self._collection.find_one({"username": user.get('username')}) is not None:
                self._collection.update_one({"username": username}, {"$set": {key: value}})
            else:
                print(f'User: {username} not find')
        except Exception as ex:
            print("[change_user] Some problem...")
            print(ex)


class CharDB(object):
    def __init__(self, host: str = MONGO_ADDRESS,
                 port: int = 27017,
                 db_name: str = MONGO_DB_NAME,
                 collection: str = MONGO_COLLECTION_CHAR):
        self._client = MongoClient(f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{host}/')
        self._collection = self._client[db_name][collection]

    def find_by_name(self, name: str):
        try:
            print({"name": {"value": name}})
            data = self._collection.find_one({"name": {"value": name}})
            print("Get char by name")
            return data
        except Exception as ex:
            print("[find_by_username] Some problem...")
            print(ex)
    def test(self):
        print('ffffff')
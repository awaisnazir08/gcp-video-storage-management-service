import pymongo

class MongoService:
    def __init__(self, uri):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client['user_management']
        self.storage_collection = self.db['video_storage']

    def find_user_storage(self, username):
        return self.storage_collection.find_one({'username': username})

    def initialize_user_storage(self, username, total_storage):
        storage = {
            'username': username,
            'total_storage': total_storage,
            'used_storage': 0,
            'files': []
        }
        self.storage_collection.insert_one(storage)
        return storage

    def update_storage(self, username, update_data):
        self.storage_collection.update_one({'username': username}, update_data)

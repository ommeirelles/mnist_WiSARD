from pymongo import *

class Profile:

    def __init__ (self, config):
        database = config["database"]
        self.db = MongoClient(config["host"], config["port"])[database]

    def insert_many (self, docs = []):
        '''
            Not make any test on docs to get more performance on writing to disk
        '''
        return self.db.Profile.insert_many(docs).inserted_ids

    def get_item (self, itemId):
        return self.db.Profile.find_one({"_id": itemId})

    def query (self, query):
        return self.db.Profile.find(query)

    def query_one (self, query):
        return self.db.Profile.find_one(query)
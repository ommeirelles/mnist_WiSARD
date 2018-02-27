from pymongo import *

class Discriminator:

    def __init__ (self, config):
        database = config["database"]
        self.db = MongoClient(config["host"], config["port"])[database]

    def insert (self, doc):
        '''
            Not make any test on docs to get more performance on write to disk
        '''
        return self.db.Discriminator.insert_one(doc).inserted_id

    def insert_many (self, docs = []):
        '''
            Not make any test on docs to get more performance on write to disk
        '''
        return self.db.Discriminator.insert_many(docs).inserted_ids

    def get_item (self, itemId):
        return db.Discriminator.find_one({"_id": itemId})
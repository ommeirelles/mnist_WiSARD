from pymongo import *

class Node:

    def __init__ (self, config):
        database = config["database"]
        self.db = MongoClient(config["host"], config["port"])[database]

    def insert (self, doc):
        '''
        # Testing model doc to not insert durty documents on mongo. 
        # I have take that part away because i have more preformance on write
        if (
            type(doc).__name__ == "dict" and
            len(doc.keys()) = 2 and
            "discriminatorId" in doc.keys() and
            type(doc["discriminatorId"]).__name__ == "ObjectId"
        ):
        '''
        return self.db.Node.insert_one(doc).inserted_id

    def insert_many (self, docs = []):
        '''
            Not make any test on docs to get more performance on write to disk
        '''
        return self.db.Node.insert_many(docs).inserted_ids

    def get_item (self, itemId):
        return db.Node.find_one({"_id": itemId})


    def query (self, query):
        return self.db.Node.find(query)
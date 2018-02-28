from discriminator import *
import pymongo

class Profile:
    def __init__ (self, nodes, description, conn):
        self.conn = conn
        self.collection = conn["Profile"]

        if type(self.collection.find_one({"nodes": nodes})).__name__ == "dict":
            raise Exception('Profile ja existente')
        else: 
            self.nodes = int(nodes)
            self.description = str(description)
            self.discriminators = []
            self.id = self.collection.insert_one({
                "nodes": self.nodes,
                "description": self.description,
                "discriminators": []
            }, True).inserted_id

    def addDiscriminators(self, labels = []):
        for i in labels:
            self.discriminators.append(Discriminator(self.nodes, 784, i, self.id, self.conn))
        self.collection.find_one_and_update({"_id": self.id}, {"$set": {
                "discriminators": [d.id for d in self.discriminators]
            }
        })

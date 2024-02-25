from src.Utils.config import Config
from pymongo import MongoClient
from typing import Dict, List
from uuid import uuid4



class Database:
    """
    Wrapper class for Mongo DB
    """

    def _init_(self):
        """
        Constructor taking database URI and instantiating db object
        """
        self.mongo_conn = MongoClient(host=Config.DATABASE_CONNECTION)
        self.db = self.mongo_conn[Config.DATABASE_NAME]

    def insert_one(self, collection: str, data: Dict):
        """
        Method to insert one document into specified collection in mongo
        """
        data["_id"] = str(uuid4())
        self.db[collection].insert_one(data)

    def insert_many(self, collection: str, data: List[Dict]):
        """
        Method to insert multiple documents into specified collection in mongo
        """
        for d in data:
            d["_id"] = str(uuid4())
        self.db[collection].insert_many(data)

    def find_one(self, collection: str, query: Dict, exclude_fields = []):
        """
        Method to find data from the given query in mongo
        """
        exclude_query = {"_id": 0}
        if exclude_fields:
            for field in exclude_fields:
                exclude_query[field] = 0
        return self.db[collection].find_one(query, exclude_query)

    def find_all(self, collection: str, query: Dict, exclude_fields = []):
        """
        Method to find all the data from the given query in mongo
        """
        exclude_query = {"_id": 0}
        if exclude_fields:
            for field in exclude_fields:
                exclude_query[field] = 0
        return self.db[collection].find(query, exclude_query)

    def update_one(self, collection: str, find_query: Dict, set_query: Dict):
        """
        Method to update data in a collection
        """
        return self.db[collection].update_one(find_query, {"$set":set_query})

    def delete_one(self, collection: str, query: Dict):
        """
        Method to delete a document inside the given collection
        """

        return self.db[collection].delete_one(query)

    def delete_all(self, collection: str, query: Dict):
        """
        Method to delete many documents inside the given collection

        """

        return self.db[collection].delete_many(query)
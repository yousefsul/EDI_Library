from pymongo import MongoClient

MONGO_CLIENT = "mongodb://yousef:Ys2021xch@209.151.150.58:63327/?authSource=admin&readPreference=primary&appname" \
               "=MongoDB%20Compass&ssl=false"


class ConnectMongoDB:
    """
    connect to devDB and client database
    define the clients_collection,visits_collection,claims_collection as none
    """

    def __init__(self):
        try:
            self.__mongo_client = MongoClient(MONGO_CLIENT)
            self.__db = self.__mongo_client.client_2731928905_DB
            self.__main_collection = None
            self.__index_collection = None
        except ConnectionError:
            print(ConnectionError, "connection error have been occured")

    def connect_to_collection(self , collection_name):
        self.__main_collection = self.__db[collection_name]

    def insert_to_main_collection(self, result):
        try:
            self.__main_collection.insert(result)
        except Exception as e:
            print("An Exception occurred ", e)

    def connect_to_index_collection(self, collection_name):
        self.__index_collection = self.__db[collection_name]

    def insert_to_index_collection(self, result):
        try:
            self.__index_collection.insert(result)
        except Exception as e:
            print("An Exception occurred ", e)



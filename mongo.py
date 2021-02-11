import pandas as pd
import pymongo as pm


def insert_to_mongodb(x):
    mongo_client = pm.MongoClient("mongodb://localhost:27017/")
    mongo_database = mongo_client["capstone_news"]
    mongo_collection = mongo_database["news"]
    mongo_collection.delete_many({})
    mongo_collection.insert_many(x)
    mongo_client.close()


if __name__ == '__main__':
    df = pd.read_json("News_Category_Dataset_v2.json", lines=True)
    print(df.head(10))
    dictionary = df.apply(lambda x: x.to_dict(), axis=1).to_list()
    print(dictionary)
    insert_to_mongodb(dictionary)
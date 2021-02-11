import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import regex as re
import pymongo as pm
stop_words = stopwords.words('english')


"""The modular code design takes inputs from the input variables described below.
The working directory is currently set to the default downloads folder. 
"""

input7 = input("Please Enter the name of the CSV file in the format xyz.csv: ")
input6 = int(input("Enter the column index counting from 0: "))
input1 = input("String to lower cases? y/n: ")
input2 = input("Apply full regex to the string? y/n: ")
input3 = input("Tokenize the string? y/n: ")
input4 = input("Remove stopwords from the string? y/n: ")
input5 = input("Convert everything to cleaned sentences? y/n: ")

def read_and_convert_mongo(client, database, collection):
    mongo_client = pm.MongoClient(client)
    mongo_database = mongo_client[database]
    mongo_collection = mongo_database[collection]
    cursor = mongo_collection.find()
    dataframe = pd.json_normalize(cursor)
    return dataframe


def convert_string(x):
    x = x.apply(str)
    return x


def lower_characters(x):
    x = x.apply(str)
    x = x.str.lower()
    return x


def apply_regex(x):
    x = x.replace("'s", '')
    x = x.replace(",", ' ')
    x = x.apply(lambda elem: elem.replace(",", ' ',))
    x = x.apply(lambda elem: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", " ", elem))
    x = x.apply(lambda elem: re.sub(r"\d+", "", elem))
    x = x.apply(lambda elem: re.sub(r"(?<=\d)(st|nd|rd|th)\b", '', elem))
    return x


def tokenize_sentences(x):
    x = x.apply(lambda elem: word_tokenize(elem))
    return x


def remove_stopwords(x):
    x = x.apply(lambda elem: [word for word in elem if not word in stop_words])
    return x


def clean_sentences(x):
    x = x.apply(lambda elem: " ".join([word for word in elem]))
    return x


if __name__ == '__main__':
    df = pd.read_csv("" + input7)
    df.iloc[:, [input6]] = df.iloc[:, [input6]].apply(lambda x: convert_string(x))
    if input1 == 'y':
        df.iloc[:, [input6]] = df.iloc[:, [input6]].apply(lambda x: lower_characters(x))
    if input2 == 'y':
        df.iloc[:, [input6]] = df.iloc[:, [input6]].apply(lambda x: apply_regex(x))
    if input3 == 'y':
        df.iloc[:, [input6]] = df.iloc[:, [input6]].apply(lambda x: tokenize_sentences(x))
    if input4 == 'y':
        df.iloc[:, [input6]] = df.iloc[:, [input6]].apply(lambda x: remove_stopwords(x))
    if input5 == 'y':
        df.iloc[:, [input6]] = df.iloc[:, [input6]].apply(lambda x: clean_sentences(x))
    print(df)
    """
    df.to_csv("forcomprehend.csv")
    """
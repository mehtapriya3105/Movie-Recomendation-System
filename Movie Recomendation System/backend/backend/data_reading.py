import pandas as pd 
from pymongo import MongoClient

#get 3 df from movie, users, ratings 
def read_data(mongo_url , mongo_db_name , mongo_collection_name):
    client = MongoClient(mongo_url) 
    db = client[mongo_db_name]  
    collection = db[mongo_collection_name]  
    data_from_mongodb = list(collection.find())
    client.close()
    df = pd.DataFrame(data_from_mongodb)
    return df

def get_data(mongo_db_name, mongo_collection_name, mongo_url=  'mongodb://localhost:27017'):
    name = read_data(mongo_url, mongo_db_name, mongo_collection_name)
    return name

def print_df_details(df):
    print(df.info())
    print(df.describe())
    print(df.head())
    
def print_df(df):
    if len(df)>0:
        return  df.to_html(index=False)
    else: 
        return  "No Data Found"
    
ratings = get_data("movie", "ratings")
movie = get_data("movie", "movie")
users = get_data("movie", "users")

#movie.info()
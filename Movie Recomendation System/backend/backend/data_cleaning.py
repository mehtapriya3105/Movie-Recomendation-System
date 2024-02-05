import pandas as pd 
import numpy as np
from data_reading import movie, ratings, users

def clean_rating_data(movie, ratings,users):
    ratings['Ratings'] = ratings['Ratings'].astype('int64')
    ratings['UserID'] = ratings['UserID'].astype('int64')
    ratings = pd.DataFrame(ratings)
    clomntoappend = movie['MovieID'] 
    ratings['MovieID'] = clomntoappend
    ratings['MovieID'] = ratings['MovieID'].fillna(0).astype('int64')
    ratings['user_emb_id'] = ratings['UserID'] - 1
    ratings['movie_emb_id'] = ratings['MovieID'] - 1
    ratings = ratings.drop("Title",axis = 1)
    ratings = ratings.drop("Timestamp",axis = 1)
    ratings = ratings.drop("user_emb_id",axis = 1)
    ratings = ratings.drop("movie_emb_id",axis = 1)
    new_order = ['UserID', 'MovieID', 'Ratings']
    ratings_new = ratings[new_order]
    ratings = ratings_new
    return ratings

def map_age_to_category(age):
    if int(age) < 18:
        return "Under 18"
    elif int(age) < 25:
        return "18-24"
    elif int(age) < 35:
        return "25-34"
    elif int(age) < 45:
        return "35-44"
    elif int(age) < 50:
        return "45-49"
    elif int(age) < 56:
        return "50-55"
    else:
        return "56+"

def clean_user_data(movie,ratings,users):
    AGES = { 1: "Under 18", 18: "18-24", 25: "25-34", 35: "35-44", 45: "45-49", 50: "50-55", 56: "56+" }
    OCCUPATIONS = { 0: "other or not specified", 1: "academic/educator", 2: "artist", 3: "clerical/admin",
                4: "college/grad student", 5: "customer service", 6: "doctor/health care",
                7: "executive/managerial", 8: "farmer", 9: "homemaker", 10: "K-12 student", 11: "lawyer",
                12: "programmer", 13: "retired", 14: "sales/marketing", 15: "scientist", 16: "self-employed",
                17: "technician/engineer", 18: "tradesman/craftsman", 19: "unemployed", 20: "writer" }
    users['Occupation'] = users['Occupation'].fillna(0).astype('int64')
    users['age_category'] = users['Age'].apply(map_age_to_category)
    users['Occupation'] = users['Occupation'].map(OCCUPATIONS)
    users['UserID'] = users['UserID'].astype('int64')
    users = users.drop('Age',axis = 1)
    new_order = ['UserID', 'Gender', 'Zip-code','age_category','Occupation' ]
    users_new = users[new_order]
    users = users_new
    return users

def clean_movie_data(movie):
    movie["Genres"] = movie["Genres"].astype('str')
    movie['MovieID'] = movie['MovieID'].astype('int64')
    movie['Genres'] = movie['Genres'].str.split('|')
    movie['Genres'] = movie['Genres'].fillna("").astype('str')
    movie["Title"] = movie["Title"].astype('str')
    return movie

def create_final_dataset(movie,ratings,users):
    dataset = pd.merge(pd.merge(movie, ratings,on = "MovieID"),users ,  on = "UserID")
    dataset["Genres"] = dataset["Genres"].astype('str')
    dataset["Title"] = dataset["Title"].astype('str')
    return dataset

movie_this = movie
ratings_this = ratings
users_this = users
ratings_cleaned = clean_rating_data(movie_this,ratings_this,users_this)
movies_cleaned = clean_movie_data(movie_this)
users_cleaned = clean_user_data(movie_this, ratings_this , users_this)
print(ratings_cleaned.info())
print(users_cleaned.info())
print(movies_cleaned.info())
final_set = create_final_dataset(movies_cleaned,ratings_cleaned,users_cleaned)
print(final_set.info())
#print("ok")
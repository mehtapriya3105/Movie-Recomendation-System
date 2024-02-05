# recommendation_logic.py
from data_cleaning import final_set
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from pymongo import MongoClient
from sklearn.metrics.pairwise import pairwise_distances




def count_word(dataset, ref_col, census):
    keyword_count = dict()
    for s in census: 
        keyword_count[s] = 0
    for census_keywords in dataset[ref_col].str.split('|'):        
        if (type(census_keywords) == float and pd.isnull(census_keywords)): 
            continue        
        for s in [s for s in census_keywords if s in census]: 
            if pd.notnull(s): 
                keyword_count[s] += 1
    keyword_occurences = []
    for k,v in keyword_count.items():
        keyword_occurences.append([k,v])
    keyword_occurences.sort(key = lambda x:x[1], reverse = True)
    return keyword_occurences, keyword_count

def create_genre_set(dataset):
    genre_labels = set()
    for s in dataset['Genres'].str.split('|').values:
        genre_labels = genre_labels.union(set(s))
    keyword_occurences, dum = count_word(dataset, 'Genres', genre_labels)
    return keyword_occurences

def tf_idf(dataset):
    tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(dataset['Genres'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim

def genre_recommendations(dataset):
    cosine_sim = tf_idf(dataset)
    titles = dataset['Title']
    indices = pd.Series(dataset.index, index=dataset['Title'])
    idx = indices[titles]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]

def content_based_filtering(dataset):
    dataset['features'] = dataset['Genres'] + ' ' + dataset['Gender'] + ' ' + dataset['age_category'] + ' ' + dataset['Occupation']
    count_vectorizer = CountVectorizer()
    feature_matrix = count_vectorizer.fit_transform(dataset['features'])
    cosine_sim = cosine_similarity(feature_matrix, feature_matrix)
    return cosine_sim

def get_content_based_recommendations(movie_title, dataset, top_n=15):

    cosine_sim_matrix = content_based_filtering(dataset)
    # Get the index of the movie in the DataFrame
    movie_index = dataset[dataset['Title'] == movie_title].index[0]

    # Get the pairwise similarity scores with other movies
    sim_scores = list(enumerate(cosine_sim_matrix[movie_index]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the top-n similar movies
    top_movie_indices = [i[0] for i in sim_scores[1:top_n+1]]

    # Get the movie titles corresponding to the indices
    top_movie_titles = dataset['Title'].iloc[top_movie_indices].tolist()

    return top_movie_titles

def get_recommendations(movie_name,dataset = final_set):
    recommendations = get_content_based_recommendations(movie_name,dataset)
    return list(recommendations)


dataset = final_set



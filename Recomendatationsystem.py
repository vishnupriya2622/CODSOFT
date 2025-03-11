import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_movies(movie_title, movies_df, top_n=5):
    if movie_title not in movies_df['title'].values:
        return "Movie not found in the dataset."
    
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies_df['description'].fillna(""))
    
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    idx = movies_df.index[movies_df['title'] == movie_title].tolist()[0]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    seen_titles = set()
    unique_recommendations = []
    
    for movie_idx, score in sim_scores:
        title = movies_df.iloc[movie_idx]['title']
        if title != movie_title and title not in seen_titles:
            seen_titles.add(title)
            unique_recommendations.append(title)
        if len(unique_recommendations) == top_n:
            break
    
    return unique_recommendations

movies_data = {
    'title': ['Inception', 'Interstellar', 'The Dark Knight', 'Memento', 'The Prestige'],
    'description': [
        "A thief who enters the dreams of others to steal secrets.",
        "A group of astronauts travel through a wormhole in search of a new home.",
        "A vigilante fights crime in Gotham city.",
        "A man with short-term memory loss uses notes and tattoos to find his wife's killer.",
        "Two magicians compete to create the best stage illusion."
    ]
}

movies_df = pd.DataFrame(movies_data)

print(recommend_movies('Inception', movies_df))

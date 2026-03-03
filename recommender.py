import pickle
import pandas as pd
import streamlit as st

# wrapping model loading inside a func using streamlit.
# This is used because:
# Model loads once
# Speeds up deployment
# Reduces memory overhead
# Makes app scalable

@st.cache_resource
def load_resources():
    # loading the model into this
    with open("model/knn_model.pkl", "rb") as f:
        model = pickle.load(f)

    # loading the scaler into this
    with open("model/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    # loading the songs df into this
    songs = pd.read_pickle("model/songs_clean.pkl")

    # features used for KNN similarity
    features = [
        'danceability',
        'energy',
        'loudness',
        'speechiness',
        'acousticness',
        'instrumentalness',
        'liveness',
        'valence',
        'tempo'
    ]

    x = songs[features]
    x_scaled = scaler.transform(x)

    return model, scaler, songs, x_scaled


model, scaler, songs, x_scaled = load_resources()



# Function for recommendation considering either id or name
def recommend(song_input, n=5, genre=None, use_popularity=True):

    # check if input is id or name
    if isinstance(song_input, str) and song_input in songs['track_id'].values:
        selected_song = songs[songs['track_id'] == song_input]
    else:
        # fuzzy match and prevents crash if null values exist
        matches = songs[
            songs['track_name'].str.lower().str.contains(song_input.lower(), na=False)
        ]

        if len(matches) == 0:
            return None

        selected_song = matches.iloc[[0]]

    idx = selected_song.index[0]

    # KNN similarity
    distances, indices = model.kneighbors(
        [x_scaled[idx]],
        n_neighbors=50
    )

    similar = songs.iloc[indices[0][1:]].copy()

    # score of similarity
    similar["similarity_score"] = 1 - distances[0][1:]

    # avoiding recommending same track id again
    similar = similar[
        similar['track_id'] != selected_song.iloc[0]['track_id']
    ]

    # avoiding same artist repetition
    similar = similar[
        similar['artists'] != selected_song.iloc[0]['artists']
    ]

    # filter by genre optional
    if genre:
        similar = similar[
            similar['track_genre'].str.lower() == genre.lower()
        ]

    if len(similar) == 0:
        return None

    # popularity filter if tie in similarity for sorting
    if use_popularity:
        similar = similar.sort_values(
            by=["similarity_score", "popularity"],
            ascending=[False, False]
        )
    else:
        similar = similar.sort_values(
            by="similarity_score",
            ascending=False
        )

    result = similar.head(n)[[
        "track_name",
        "artists",
        "album_name",
        "track_genre",
        "popularity",
        "similarity_score",
        "track_id"
    ]]

    return result




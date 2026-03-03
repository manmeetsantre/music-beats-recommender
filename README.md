# 🎵 MUSIC BEATS – Song Recommendation System

A Content-Based Music Recommendation System built using:

- Python  
- Scikit-learn (K-Nearest Neighbors)  
- Streamlit  
- Spotify API (Spotipy)  
- Feature Scaling (StandardScaler)

This app recommends songs similar to a selected track based on audio features.

---

## 🚀 Live Demo

👉 Deployed on Streamlit Cloud  
(Add your live link here after deployment)

---

## 🧠 Project Overview

This system:

- Uses Spotify audio features (danceability, energy, tempo, etc.)
- Applies feature scaling using StandardScaler
- Uses K-Nearest Neighbors (KNN) for similarity search
- Ranks recommendations by similarity + popularity
- Provides optional genre filtering
- Fetches album artwork and preview using Spotify API
- Displays results via a clean Streamlit UI

---

## 📁 Project Structure


Song_Recommender/
│
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
│
└── model/
├── knn_model.pkl
├── scaler.pkl
└── songs_clean.pkl


---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd Song_Recommender
2️⃣ Ensure Python 3.12 is Installed

Check version:

py -3.12 --version
3️⃣ Install Required Dependencies
py -3.12 -m pip install -r requirements.txt
4️⃣ Add Spotify API Credentials

Create:

.streamlit/secrets.toml

Add:

CLIENT_ID = "your_spotify_client_id"
CLIENT_SECRET = "your_spotify_client_secret"
5️⃣ Run the Application
py -3.12 -m streamlit run app.py

Open in browser:

http://localhost:8501
🔍 How It Works
Step 1 – Load Saved Model

The system loads:

Trained KNN model

StandardScaler

Cleaned songs dataset

Using @st.cache_resource to improve performance.

Step 2 – Feature Processing

Selected audio features:

danceability

energy

loudness

speechiness

acousticness

instrumentalness

liveness

valence

tempo

These are scaled using the saved StandardScaler.

Step 3 – Song Matching

User can input:

Track Name
OR

Track ID

System:

Matches the track

Retrieves its feature vector

Finds nearest neighbors using KNN

Step 4 – Filtering Logic

The system:

Removes the original song

Avoids recommending same artist

Applies optional genre filter

Sorts by similarity score

Breaks ties using popularity

Step 5 – UI Display

Each recommendation displays:

Album Artwork

Track Name

Artist

Album

Genre

Popularity

Similarity Score

Spotify Link

Preview (if available)

🖥️ Features

✔ Content-Based Filtering
✔ KNN Similarity Model
✔ Feature Scaling
✔ Genre Filtering
✔ Popularity-Based Ranking
✔ Spotify API Integration
✔ Optimized Caching
✔ Production-Ready Deployment
✔ Clean & Modern UI
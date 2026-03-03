# 🎵 MUSIC BEATS 🎵  
## Content-Based Music Recommendation System

A production-ready content-based music recommendation system built using:

- Python  
- Scikit-learn (K-Nearest Neighbors)  
- Streamlit  
- Spotify API (Spotipy)  
- Feature Scaling (StandardScaler)  

This app recommends songs similar to a selected track using Spotify audio features and similarity modeling.

---

## 🚀 Live Demo

👉 **Live App:**  
https://music-beats.streamlit.app  

Deployed on Streamlit Cloud.

---

## 🧠 Project Overview

This system:

- Uses Spotify audio features (danceability, energy, tempo, etc.)
- Applies feature scaling using StandardScaler
- Uses K-Nearest Neighbors (KNN) for similarity computation
- Ranks recommendations by similarity + popularity
- Provides optional genre filtering
- Fetches album artwork and preview using Spotify API
- Displays results through a clean Streamlit UI
- Uses caching to optimize performance

---

## 📁 Project Structure

```
music-beats-recommender/
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
```

---

## ⚙️ Setup Instructions (Local Development)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/manmeetsantre/music-beats-recommender.git
cd music-beats-recommender
```

---

### 2️⃣ Ensure Python 3.12 Is Installed

```bash
py -3.12 --version
```

---

### 3️⃣ Install Required Dependencies

```bash
py -3.12 -m pip install -r requirements.txt
```

---

### 4️⃣ Add Spotify API Credentials

Create the following file:

```
.streamlit/secrets.toml
```

Add:

```
CLIENT_ID = "your_spotify_client_id"
CLIENT_SECRET = "your_spotify_client_secret"
```

⚠ **Do NOT commit this file to GitHub.**

---

### 5️⃣ Run the Application

```bash
py -3.12 -m streamlit run app.py
```

Open in your browser:

```
http://localhost:8501
```

---

## 🔍 How It Works

### Step 1 – Load Saved Model

The system loads:

- Trained KNN model  
- StandardScaler  
- Cleaned songs dataset  

Using `@st.cache_resource` for improved performance.

---

### Step 2 – Feature Processing

Selected audio features:

- danceability  
- energy  
- loudness  
- speechiness  
- acousticness  
- instrumentalness  
- liveness  
- valence  
- tempo  

These are scaled using the saved StandardScaler before similarity computation.

---

### Step 3 – Song Matching

User can input:

- Track Name  
- OR Track ID  

The system:

- Matches the selected song  
- Retrieves its feature vector  
- Finds nearest neighbors using KNN  

---

### Step 4 – Filtering Logic

The system:

- Removes the original song from results  
- Avoids recommending songs from the same artist  
- Applies optional genre filter  
- Sorts by similarity score  
- Breaks ties using popularity  

---

### Step 5 – UI Display

Each recommendation includes:

- Album Artwork  
- Track Name  
- Artist  
- Album  
- Genre  
- Popularity  
- Similarity Score  
- Spotify Link  
- 30-second Preview (if available)  

---

## 🖥️ Features

- ✔ Content-Based Filtering  
- ✔ KNN Similarity Model  
- ✔ Feature Scaling  
- ✔ Genre Filtering  
- ✔ Popularity-Based Ranking  
- ✔ Spotify API Integration  
- ✔ Optimized Caching  
- ✔ Production Deployment via Streamlit Cloud  
- ✔ Clean & Modern UI  

---

## 🏗 Tech Stack

- Python 3.12  
- Streamlit  
- Scikit-learn  
- Pandas  
- NumPy  
- Spotipy  

---

## 📦 Deployment

Deployed using:

- GitHub (Version Control)  
- Streamlit Cloud (Hosting)  

Planned production upgrades:

- Docker containerization  
- CI/CD with GitHub Actions  
- AWS deployment (EC2 / ECS)  
- Authentication layer  

---

## 📌 Future Improvements

- User authentication  
- Playlist export feature  
- Advanced filtering (mood, tempo range)  
- Model retraining pipeline  
- Docker + AWS production deployment  
- CI/CD automation  

---

## 👨‍💻 Author

Built by **Manmeet Santre**

---

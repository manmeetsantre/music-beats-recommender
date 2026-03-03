import streamlit as st
import time  # for loading animation

# spotify api connect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from recommender import recommend


# setting browser title and icon
st.set_page_config(
    page_title="MUSIC BEATS",
    page_icon="🎵"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.song-title {
    margin-top: 0px !important;
    margin-bottom: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# Spotify API credentials from secrets
CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["CLIENT_SECRET"]

auth_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

sp = spotipy.Spotify(auth_manager=auth_manager)


# function to fetch spotify metadata
def get_spotify_data(track_name, artist):

    query = f"track:{track_name} artist:{artist}"
    results = sp.search(q=query, type="track", limit=1)

    if results["tracks"]["items"]:
        track = results["tracks"]["items"][0]

        # image extraction
        image = None
        if track["album"]["images"]:
            image = track["album"]["images"][0]["url"]

        # preview extraction
        preview = track.get("preview_url", None)

        # spotify url
        spotify_url = track["external_urls"].get("spotify", None)

        return image, preview, spotify_url

    return None, None, None


st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #aaa;
    margin-bottom: 30px;
}
@media (max-width: 768px) {
    .main-title {
        font-size: 30px;
    }
    .subtitle {
        font-size: 14px;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>MUSIC BEATS</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>🎧 Find songs similar to your vibe 🎧</div>", unsafe_allow_html=True)

song_input = st.text_input("Enter Name or ID of the Song")
genre = st.text_input("Enter the genre (Optional)")
n = st.slider("Number of Recommendations", 1, 10, 5)

# aligning button in center
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    recommend_btn = st.button("Recommend Songs", use_container_width=True)


if recommend_btn:

    # preventing empty search
    if not song_input.strip():
        st.warning("Please enter a song name or track ID")
        st.stop()

    with st.spinner("Finding similar songs..."):
        time.sleep(1)
        result = recommend(song_input, n=n, genre=genre)

    if result is not None:

        st.markdown("---")

        for _, row in result.iterrows():

            image, preview, spotify_url = get_spotify_data(
                row["track_name"], row["artists"]
            )

            col1, col2 = st.columns([1.2, 2.8], gap="medium", vertical_alignment="top")

            with col1:
                # st.markdown(
                #     "<div style='display:flex; align-items:flex-start;'>",
                #     unsafe_allow_html=True
                # )
                if image:
                    st.markdown(
                        f"""
                        <img src="{image}" 
                        style="width:100%; border-radius:10px; display:block; margin:0; padding:0;">
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        """
                        <img src="https://via.placeholder.com/300x300?text=No+Image" 
                        style="width:100%; border-radius:10px; display:block; margin:0; padding:0;">
                        """,
                        unsafe_allow_html=True
                    )
                # st.markdown("</div>", unsafe_allow_html=True)

            with col2:
                st.markdown(
                    f"""
                    <div style="
                        font-size:22px;
                        font-weight:700;
                        line-height:1;
                        margin:0;
                        padding:0;
                    ">
                        {row['track_name']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown(f"**Artist:** {row['artists']}")
                st.markdown(f"**Album:** {row['album_name']}")
                st.markdown(f"**Genre:** {row['track_genre']}")
                st.markdown(f"**Popularity:** {row['popularity']}")
                st.markdown(f"**Similarity:** {round(row['similarity_score'], 4)}")

                if spotify_url:
                    st.markdown(f"[Open in Spotify]({spotify_url})")

                if preview:
                    st.audio(preview)
                else:
                    st.caption("Preview not available")

                # st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("---")

    else:
        st.write("Sorry! No results found in the collection.")


# footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>Built with ❤️ for music listeners!</p>",
    unsafe_allow_html=True
)

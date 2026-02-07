import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set page configuration
st.set_page_config(page_title="Happy Rose Day!", page_icon="🌹", layout="centered")

# Custom CSS for the Valentine's vibe
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    .main-title {
        font-family: 'Dancing Script', cursive;
        color: #ff4d6d;
        text-align: center;
        font-size: 3.5rem;
        font-weight: bold;
        padding-top: 20px;
        text-shadow: 2px 2px #ffb3c1;
    }
    .sub-text {
        text-align: center;
        color: #c9184a;
        font-size: 1.2rem;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# A beautiful blooming rose animation
lottie_rose = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_S69rU8.json")

# Website Content
st.markdown('<p class="main-title">Happy Rose Day Jaanuuuuuuu <3</p>', unsafe_allow_html=True)

# Display the popping rose
if lottie_rose:
    st_lottie(lottie_rose, height=400, key="rose")

st.markdown('<p class="sub-text">Every rose has its thorn, but you are the rose that makes life beautiful.</p>', unsafe_allow_html=True)

# Interactive button for an extra surprise
if st.button("Click for a hug! 🤗"):
    st.balloons()
    st.snow()  # Looks like falling petals if you imagine hard enough!
    st.write("❤️ I love you so much! ❤️")

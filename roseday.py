import streamlit as st

# Set page configuration
st.set_page_config(page_title="Happy Rose Day!", page_icon="🌹", layout="centered")

# Custom CSS for the Valentine's vibe
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    .main-title {
        color: #ff4d6d;
        text-align: center;
        font-size: 3.5rem;
        font-weight: bold;
        text-shadow: 2px 2px #ffb3c1;
    }
    .sub-text {
        text-align: center;
        color: #c9184a;
        font-size: 1.5rem;
        font-style: italic;
    }
    div.stButton > button {
        background-color: #ff4d6d;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown('<p class="main-title">Happy Rose Day Jaanuuuuuuu <3</p>', unsafe_allow_html=True)

# Big Rose Image (Using a direct link so no extra libraries needed)
st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3UzbzU4eW13eWN6c3FucDFnaDNveW9mOHM2OWc5Nm5kNnd3eWdpZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Zl7u48zLVFgLpRwq6f/giphy.gif", use_container_width=True)

st.markdown('<p class="sub-text">Happy rose day my lil cutie pie rosey plum cupcake honeybun yummy in my tummy sweetu. 🌹</p>', unsafe_allow_html=True)

# Interactive button
if st.button("Click for a surprise! 🤗"):
    st.balloons()
    st.markdown("<h2 style='text-align: center; color: #ff4d6d;'>❤️ I love you so much! ❤️</h2>", unsafe_allow_html=True)

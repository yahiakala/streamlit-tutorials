import streamlit as st
from PIL import Image

st.write("""
# Simple App

Hey there! Welcome to the app!

I'm so glad you're here!

""")

# Run on save.

# Put your code in a github repo (include refs in readme)

# Markdown cheatsheet
# Page 1: Training the model
# - show the training data
# - show the testing data
# - show the model performance

# Page 2: Using the model
# - upload a photo
# - photo gets displayed
# - steps to process the photo are shown.

uploaded_file = st.file_uploader("Upload your profile picture.",
                                 type=['jpg', 'png'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, width=500)
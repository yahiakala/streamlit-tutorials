import streamlit as st
from PIL import Image
from detect_smile_image import detect_smile
import cv2
import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True


cascade = 'haarcascade_frontalface_default.xml'
model = './model2.h5'
pic_backup = './sample_photos/mai_smile.jpg'

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
                                 type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    print(uploaded_file)
    st.image(image, width=500)
    label = detect_smile(cascade, model, pic_backup)
    st.write(label)

# Button to train model and then display output
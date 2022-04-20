import streamlit as st
from PIL import Image, ImageOps
from detect_smile_image import detect_smile
import cv2

try:
    import keras.backend.tensorflow_backend as tb
    tb._SYMBOLIC_SCOPE.value = True
except ModuleNotFoundError:
    pass


cascade = 'haarcascade_frontalface_default.xml'
model = './model2.h5'
pic_backup = './sample_photos/mai_smile.jpg'

st.write("""
# Smile Detector App

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

# Page: Detailed model output
# Look at each step.
# Show some examples of smiles, some examples of non smiles

# Page: upload data to a db?

# UploadedFile class object.
uploaded_file = st.file_uploader("Upload your profile picture.",
                                 type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    fixed_image = ImageOps.exif_transpose(image)
    st.image(fixed_image, width=500)
    # st.write(uploaded_file)
    label = detect_smile(cascade, model, fixed_image)
    st.write(label)

# Button to train model and then display output
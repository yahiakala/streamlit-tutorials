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


def app():
    st.write("""
    # Smile Detector App

    Hey there! Welcome to the app home page!

    I'm so glad you're here!

    """)
    uploaded_file = st.file_uploader("Upload your profile picture.",
                                 type=['jpg', 'png', 'jpeg'])

    if uploaded_file:
        image = Image.open(uploaded_file)
        fixed_image = ImageOps.exif_transpose(image)  # For mobile
        st.image(fixed_image)
        label = detect_smile(cascade, model, fixed_image)
        st.write(label)
        


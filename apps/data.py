import streamlit as st

# Exploration of the data?
# Explain how an image turns into an array
# Explain how the image is processed for the algorithm
# Explain how the lower resolution works
# Explain how features are extracted from the image.
# interactive element: change pixel size
# interactive: show number matrix along with image you uploaded. can also color the cells.
# some stuff about the lenet model?
# Identifying edges (sharp change in color)
# - prewitt kernel?
# --
# import numpy as np
# from skimage.io import imread, imshow
# from skimage.filters import prewitt_h,prewitt_v
# import matplotlib.pyplot as plt
# %matplotlib inline

# #reading the image 
# image = imread('puppy.jpeg',as_gray=True)

# #calculating horizontal edges using prewitt kernel
# edges_prewitt_horizontal = prewitt_h(image)
# #calculating vertical edges using prewitt kernel
# edges_prewitt_vertical = prewitt_v(image)

# imshow(edges_prewitt_vertical, cmap='gray')
# --
# expander

def app():
    st.title('Exploratory Data Analysis')
    
    st.write("""
    ## Image Data: What is it?
    Image data is not like
    
    """)
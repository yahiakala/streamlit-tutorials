import streamlit as st
from multiapp import MultiApp
from apps import home, data, model

try:
    import keras.backend.tensorflow_backend as tb
    tb._SYMBOLIC_SCOPE.value = True
except ModuleNotFoundError:
    pass

app = MultiApp()


st.write("""
# Smile Detector Project

""")

app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Model", model.app)

app.run()
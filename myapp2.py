import streamlit as st
from multiapp import MultiApp
from apps import home, data, model, training


try:
    import keras.backend.tensorflow_backend as tb
    tb._SYMBOLIC_SCOPE.value = True
except ModuleNotFoundError:
    pass

app = MultiApp()


st.write("""
# Smile Detector Project

""")

# https://icons.getbootstrap.com/
app.add_app("Home", home.app, 'house-fill')
app.add_app("Data", data.app, 'bar-chart-line-fill')
app.add_app("Training", training.app, 'clock-fill')
# app.add_app("Model", model.app, 'diagram-3-fill')

app.run()
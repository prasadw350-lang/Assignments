import streamlit as st
import numpy as np
import joblib

model = joblib.load("Best_Model.pkl")

st.title("Iris Flower Prediction")

sl = st.number_input("Sepal Length")
sw = st.number_input("Sepal Width")
pl = st.number_input("Petal Length")
pw = st.number_input("Petal Width")

if st.button("Predict"):

    prediction = model.predict([[sl,sw,pl,pw]])

    classes = [
        "Setosa",
        "Versicolor",
        "Virginica"
    ]

    st.success(
        classes[prediction[0]]
    )


    
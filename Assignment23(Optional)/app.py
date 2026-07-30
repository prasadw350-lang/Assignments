import streamlit as st
import pandas as pd
import joblib

st.title("AI Classification & Regression Predictor")

problem = st.sidebar.selectbox(
    "Select Problem",
    ["Classification", "Regression"]
)

if problem == "Classification":

    algorithm = st.selectbox(
        "Select Algorithm",
        [
            "Logistic Regression",
            "KNN",
            "Naive Bayes"
        ]
    )

    models = {
        "Logistic Regression": "LR_Model.pkl",
        "KNN": "KNN_Model.pkl",
        "Naive Bayes": "NaiveBayes_Model.pkl"
    }

    model = joblib.load(models[algorithm])
    scaler = joblib.load("LogisticRegression_Scaler.pkl")
    columns = joblib.load("LogisticRegression_Columns.pkl")

    st.subheader("Enter Mushroom Features")

    data = {}

    for col in columns:
        data[col] = st.number_input(col, value=0)

    if st.button("Predict"):

        input_df = pd.DataFrame([data])

        input_scaled = scaler.transform(input_df)

        prediction = model.predict(input_scaled)

        if prediction[0] == 0:
            st.success("🍄 Edible Mushroom")
        else:
            st.error("☠️ Poisonous Mushroom")

else:

    model = joblib.load("LR_Model.pkl")
    scaler = joblib.load("LR_Scaler.pkl")
    columns = joblib.load("LR_Columns.pkl")

    st.subheader("Enter Insurance Details")

    data = {}

    for col in columns:

        if col in ["age", "bmi", "children"]:
            data[col] = st.number_input(col, value=0.0)
        else:
            data[col] = st.number_input(col, value=0)

    if st.button("Predict Charges"):

        input_df = pd.DataFrame([data])

        input_df[["age", "bmi", "children"]] = scaler.transform(
            input_df[["age", "bmi", "children"]]
        )

        prediction = model.predict(input_df)

        st.success(f"Predicted Charges: ₹{prediction[0]:.2f}")




        
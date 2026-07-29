import streamlit as st
import pandas as pd
import joblib

st.title("AIML Multi-Model Prediction App")

problem = st.sidebar.selectbox(
    "Select Problem Type",
    ["Classification", "Regression"]
)
if problem == "Classification":

    algorithm = st.selectbox(
        "Select Algorithm",
        [
            "Logistic Regression",
            "Decision Tree",
            "SVM",
            "KNN",
            "Naive Bayes"
        ]
    )

    models = {
        "Logistic Regression": "Logistic_Regression.pkl",
        "Decision Tree": "Decision_Tree_Classifier.pkl",
        "SVM": "SVM_Classifier.pkl",
        "KNN": "KNN_Classifier.pkl",
        "Naive Bayes": "Naive_Bayes.pkl"
    }

    model = joblib.load(models[algorithm])

    scaler = joblib.load("Classification_Scaler.pkl")

    columns = joblib.load("Classification_Columns.pkl")

    st.subheader("Enter Feature Values")

    data = {}

    for col in columns:
        data[col] = st.number_input(col, value=0)

    if st.button("Predict"):

        input_df = pd.DataFrame([data])

        input_scaled = scaler.transform(input_df)

        prediction = model.predict(input_scaled)

        if prediction[0] == 0:
            st.success("Edible Mushroom")
        else:
            st.error("Poisonous Mushroom")

else:

    algorithm = st.selectbox(
        "Select Algorithm",
        [
            "Linear Regression",
            "Decision Tree Regressor",
            "SVR",
            "KNN Regressor"
        ]
    )

    models = {
        "Linear Regression": "Linear_Regression.pkl",
        "Decision Tree Regressor": "Decision_Tree_Regressor.pkl",
        "SVR": "SVR.pkl",
        "KNN Regressor": "KNN_Regressor.pkl"
    }

    model = joblib.load(models[algorithm])

    scaler = joblib.load("Regression_Scaler.pkl")

    columns = joblib.load("Regression_Columns.pkl")

    st.subheader("Enter Feature Values")

    data = {}

    for col in columns:
        data[col] = st.number_input(col, value=0.0)

    if st.button("Predict"):

        input_df = pd.DataFrame([data])

        input_df[["age", "bmi", "children"]] = scaler.transform(
            input_df[["age", "bmi", "children"]]
        )

        prediction = model.predict(input_df)

        st.success(f"Predicted Charges: {prediction[0]:.2f}")
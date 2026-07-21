## Heart Disease Prediction Project

### Goal
The goal of this project is to build a machine learning model to predict heart disease based on various patient attributes.

### Data Source
The dataset used for this project is `heart.csv`, which is expected to be mounted from Google Drive at `/content/drive/MyDrive/heart.csv`.

### Methodology
1.  **Data Loading and Preprocessing**: The `heart.csv` dataset is loaded using pandas. Categorical features are one-hot encoded using `pd.get_dummies()`. The target variable `HeartDisease` is separated from the features.
2.  **Train-Test Split**: The dataset is split into training and testing sets (80% train, 20% test) to evaluate model performance.
3.  **Feature Scaling**: Features are scaled using `StandardScaler` to normalize their ranges, which is beneficial for models like Logistic Regression.
4.  **Model Training**: A `LogisticRegression` model from `sklearn` is trained on the preprocessed and scaled training data.
5.  **Prediction**: The trained model is used to make predictions on the test set.
6.  **Model Evaluation**: The model's performance is evaluated using a confusion matrix, accuracy, precision, recall, and F1-score.
7.  **Model Persistence**: The trained model, column names, and the scaler object are saved using `joblib` for future use.
8.  **Prediction on Sample Data**: A sample patient's data is used to demonstrate how to make a prediction with the saved model.

### Results
The Logistic Regression model achieved an accuracy of approximately 85.3% on the test set. Detailed metrics are available in the notebook, including:
-   **Accuracy**: 0.853
-   **Precision**: 0.900
-   **Recall**: 0.841
-   **F1 Score**: 0.869

### Usage
To use this notebook:
1.  Ensure `heart.csv` is available in your Google Drive at `/content/drive/MyDrive/heart.csv`.
2.  Run all cells sequentially.
3.  Modify the 'Sample Patient' section to test predictions for different patient profiles.
# Ford Car Price Prediction

This notebook demonstrates a machine learning pipeline to predict Ford car prices based on various features.

## Project Description

This project aims to build a linear regression model to predict the selling price of Ford cars. The dataset includes features such as year, mileage, tax, mpg, engine size, model, transmission, and fuel type.

## Setup and Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas scikit-learn joblib
    ```

3.  **Data:** Ensure the `ford_car_dataset.csv` file is accessible at the specified `filepath` (e.g., in Google Drive if using Colab).

## Usage

Run through the cells of this Colab notebook sequentially to:

1.  Load and preprocess the dataset.
2.  Perform one-hot encoding for categorical features.
3.  Standardize numerical features.
4.  Split the data into training and testing sets.
5.  Train a Linear Regression model.
6.  Evaluate the model's performance using R2 score.
7.  Save the trained model, scaler, and column names for future use.

## Model Details

*   **Model Type:** Linear Regression
*   **Libraries Used:** pandas, scikit-learn, joblib
*   **Preprocessing Steps:** One-Hot Encoding, StandardScaler

## Files

*   `ford_car_dataset.csv`: The raw dataset containing car features and prices.
*   `LR_ford_car.pkl`: The saved Linear Regression model.
*   `scaler.pkl`: The saved StandardScaler object.
*   `columns.pkl`: A list of column names used during training.

## Results

The trained model achieved an R2 score of approximately 0.84, indicating a reasonably good fit to the data.

# House Price Prediction

A Machine Learning project for predicting house prices using housing-related features. The project covers data cleaning, exploratory data analysis, feature scaling, model training, evaluation, and model comparison.

## Project Objective

The objective of this project is to build a machine learning regression model that predicts house prices based on different housing-related features.

## Dataset

The dataset contains **5,000 records** and **5 input features**.

### Features

* Average Area Income
* Average Area House Age
* Average Area Number of Rooms
* Average Area Number of Bedrooms
* Area Population

### Target Variable

* Price

## Project Workflow

1. Data Loading
2. Data Inspection
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Saving the Cleaned Dataset
6. Train-Test Split
7. Feature Scaling
8. Model Training
9. Model Evaluation
10. Model Comparison
11. Best Model Selection
12. Model Saving

## Machine Learning Models

The following regression models were trained and compared:

* Linear Regression
* Random Forest Regressor

## Model Evaluation

The models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

### Results

| Model             |       MAE |               MSE |       RMSE |   R² Score |
| ----------------- | --------: | ----------------: | ---------: | ---------: |
| Linear Regression | 80,879.10 | 10,089,009,299.50 | 100,444.06 | **0.9180** |
| Random Forest     | 94,511.34 | 14,391,497,208.58 | 119,964.57 |     0.8830 |

### Best Model

**Linear Regression** performed better on the test dataset.

* **R² Score:** 0.9180
* **RMSE:** 100,444.06

The trained Linear Regression model and StandardScaler were saved using Joblib.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Joblib
* Jupyter Notebook

## Project Structure

```text
House-Price-Prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── clean_housing.csv
│
├── models/
│   ├── linear_regression_model.pkl
│   └── standard_scaler.pkl
│
├── house_price_prediction.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project directory

```bash
cd House-Price-Prediction
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Open the Jupyter Notebook

```bash
jupyter notebook
```

Open `house_price_prediction.ipynb` and run the cells sequentially.

## Key Learning Outcomes

* Data cleaning and preprocessing
* Exploratory Data Analysis
* Train-test splitting
* Feature scaling using StandardScaler
* Regression model training
* Model evaluation and comparison
* Saving trained ML models using Joblib

## Future Improvements

* Hyperparameter tuning
* Testing additional regression algorithms
* Building a user interface for predictions
* Deploying the trained model as a web application

## Author

**Tanvi Shinde**

B.Tech Data Science 

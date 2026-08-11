# 🏡 House Price Prediction

A Machine Learning web application that predicts the estimated market price of a house based on property and surrounding-area characteristics.

The project uses **Linear Regression** with **StandardScaler** and provides an interactive **Streamlit** interface for real-time house price prediction.

---

## 🚀 Live Demo

🔗 **Streamlit App:** https://housepriceprediction-09.streamlit.app/

---

## 📌 Project Objective

The objective of this project is to build an end-to-end Machine Learning application that can:

* Predict house prices using property-related features
* Apply data preprocessing and feature scaling
* Use a trained Linear Regression model for prediction
* Convert predicted prices from USD to INR
* Provide an interactive and user-friendly web interface
* Deploy the Machine Learning application using Streamlit

---

## 🧠 Machine Learning Approach

The application uses **Linear Regression** to estimate house prices.

### Input Features

| Feature                             | Description                             |
| ----------------------------------- | --------------------------------------- |
| 💰 Average Area Income              | Average income of residents in the area |
| 🏚️ Average Area House Age          | Average age of houses in the area       |
| 🛋️ Average Area Number of Rooms    | Average number of rooms                 |
| 🛏️ Average Area Number of Bedrooms | Average number of bedrooms              |
| 👥 Area Population                  | Population of the surrounding area      |

### Prediction Pipeline

```text
User Input
    ↓
Feature Scaling
    ↓
StandardScaler
    ↓
Linear Regression Model
    ↓
Predicted House Price
    ↓
USD → INR Conversion
    ↓
Display Result
```

---

## ✨ Features

* 🏡 Interactive house price prediction
* 🔮 Real-time prediction using a trained ML model
* 💰 Price displayed in USD
* 🇮🇳 Price converted and displayed in INR
* 📊 Property summary after prediction
* 🔄 Reset input values option
* 🎨 Modern and responsive Streamlit UI
* 🤖 Linear Regression based prediction
* ⚡ Fast prediction using saved model files

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Linear Regression
* StandardScaler

### Data & Numerical Computing

* NumPy

### Model Serialization

* Joblib

### Web Application

* Streamlit

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── models/
    ├── linear_regression_model.pkl
    └── standard_scaler.pkl
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/House-Price-Prediction.git
```

### 2. Navigate to the project directory

```bash
cd House-Price-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Example Prediction

For example, the application accepts values such as:

```text
Average Area Income        → 60000
Average Area House Age    → 5
Average Area Rooms        → 6
Average Area Bedrooms     → 3
Area Population           → 35000
```

The trained model processes these values and returns an estimated house price.

The application displays the result in both:

* 🇺🇸 USD
* 🇮🇳 INR

---

## 🔄 Reset Function

The **Reset Input Values** button restores the default input values:

```text
Average Area Income        → 60000
Average Area House Age    → 5
Average Area Rooms        → 6
Average Area Bedrooms     → 3
Area Population           → 35000
```

This allows users to quickly start a new prediction.

---

## 📈 Model Information

**Algorithm:** Linear Regression

**Preprocessing:** StandardScaler

The input features are scaled before being passed to the trained Linear Regression model.

The trained model and scaler are saved using **Joblib** and loaded by the Streamlit application at runtime.

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Deployment Stack

```text
GitHub
   ↓
Streamlit Community Cloud
   ↓
Streamlit Application
```

---

## 🔮 Future Improvements

Possible future enhancements include:

* 📊 Add interactive data visualizations
* 📈 Add model performance metrics
* 💱 Use a live USD/INR exchange rate
* 🏘️ Add more property-related features
* 🤖 Compare multiple regression algorithms
* 📱 Further optimize the interface for mobile devices
* 📉 Display prediction confidence or an estimated price range

---

## 🎯 Learning Outcomes

Through this project, I worked with:

* Data preprocessing
* Feature scaling
* Linear Regression
* Model training and serialization
* Machine Learning prediction pipelines
* Streamlit application development
* Git and GitHub
* Cloud deployment

---

## 👩‍💻 Author

**Tanvi Shinde**

B.Tech Data Science 

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

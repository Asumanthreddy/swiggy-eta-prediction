# 🚴 Delivery Time (ETA) Prediction System for Swiggy

## 📌 Project Overview

This project predicts food delivery time (ETA) for Swiggy using Machine Learning.  
The model estimates how many minutes an order will take based on distance, traffic, weather, rider details, and order characteristics.

Accurate ETA prediction is critical for improving customer satisfaction, reducing cancellations, and optimizing logistics operations.

---

## 🎯 Business Problem

Swiggy must display reliable Estimated Time of Arrival (ETA) to customers.  
Inaccurate ETAs can lead to:

- Poor user experience
- Increased cancellations
- Operational inefficiencies

This system uses historical delivery data to learn patterns and generate accurate delivery time predictions.

---

## 🤖 Machine Learning Problem Type

- **Type:** Supervised Learning  
- **Category:** Regression  
- **Target Variable:** `time_taken` (Delivery duration in minutes)

---

## 📊 Dataset Description

The dataset contains historical Swiggy order and delivery records including:

- Distance between restaurant and delivery location
- Traffic conditions
- Weather conditions
- Rider details (age, ratings, vehicle condition)
- Order information (type, time, date)
- Location coordinates

---

## 🧹 Data Preprocessing

Performed the following steps:

- Column name normalization
- Missing value treatment
- Categorical variable encoding
- Feature scaling
- Outlier analysis using IQR method

---

## 🧠 Feature Engineering

Created additional predictive features:

- `is_peak_hour` → Captures rush hour effects  
- `delivery_load` → Rider workload estimation  
- `high_demand_day` → Weekend + Festival interaction  
- Temporal features (month, day, time-of-day)

---

## 📈 Exploratory Data Analysis (EDA)

Analyzed:

- Distribution of delivery time
- Impact of traffic & distance
- Outlier detection
- Feature relationships

Key insight:

> Traffic conditions strongly influence delivery time.

---

## 🏆 Models Implemented

- Linear Regression (Baseline)
- K-Nearest Neighbors (KNN)
- Random Forest Regressor
- Gradient Boosting Regressor

---

## 📏 Evaluation Metrics

Used regression metrics:

- **RMSE (Root Mean Squared Error)**
- **MAE (Mean Absolute Error)**
- **R² Score (Model Fit Quality)**

Final model achieved strong predictive performance with high R².

---

## ⚙️ Hyperparameter Tuning

Optimized model parameters using **GridSearchCV**:

- Number of trees
- Tree depth
- Split constraints
- Feature selection

---

## 🌐 Deployment

Built an interactive web application using **Streamlit**.

Workflow:

User Input → Preprocessing → Trained Model → ETA Prediction

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn
- Streamlit
- Joblib
- Matplotlib / Seaborn

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
streamlit run swiggy_app.py


---

# ✅ **requirements.txt (IMPORTANT FOR GITHUB)**

Create file **`requirements.txt`**:

```txt
numpy
pandas
scikit-learn
streamlit
joblib
matplotlib
seaborn

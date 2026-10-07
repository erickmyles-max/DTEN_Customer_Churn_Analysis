# Telco Customer Churn Analysis and Prediction

## Project Overview

This project was completed as part of the **Data Science & Analytics Internship at Daryl Tech & Educational Network (DTEN)**.

The objective of the project is to analyze telecommunications customer churn, identify important patterns associated with customers leaving the company, build machine learning models for churn prediction, and develop an interactive dashboard for exploring the results.

The project covers all three internship tasks:

1. Exploratory Data Analysis (EDA)
2. Predictive Model Building
3. Interactive Insights Dashboard


## Dataset

The project uses the **Telco Customer Churn** dataset.

The dataset contains information about telecommunications customers, including:

- Customer demographics
- Account information
- Contract type
- Internet service
- Payment method
- Monthly charges
- Total charges
- Customer tenure
- Subscription services
- Churn status

The target variable is `Churn`, which indicates whether a customer left the telecommunications company.

Public dataset source:

https://github.com/IBM/telco-customer-churn-on-icp4d


# Task 1: Exploratory Data Analysis

## Objective

The purpose of the exploratory data analysis was to clean, understand, and visualize the dataset in order to identify patterns associated with customer churn.

## Data Cleaning

The following preprocessing steps were performed:

- Inspected the dataset structure and data types
- Checked for missing values
- Checked for duplicate observations
- Converted `TotalCharges` from text to numeric format
- Handled missing `TotalCharges` values
- Created a binary version of the churn variable for analysis
- Removed the customer ID from the modeling data because it does not provide meaningful predictive information


## Exploratory Analysis

The analysis investigated relationships between customer churn and variables such as:

- Contract type
- Customer tenure
- Internet service
- Monthly charges
- Payment method
- Total charges
- Customer characteristics

Visualizations were created using **Matplotlib** and **Seaborn**.


## Key Findings

### 1. Contract Type and Churn

Customers using month-to-month contracts showed substantially higher churn than customers using longer-term contracts.

Customers with one-year and two-year contracts were less likely to churn.

### 2. Customer Tenure

Customers with shorter tenure showed a greater tendency to churn.

Customers who remained with the company for longer periods generally demonstrated lower churn.

### 3. Internet Service

Churn patterns differed across internet service categories.

In particular, customers using fiber optic internet displayed different churn behavior compared with customers using DSL or no internet service.

### 4. Monthly Charges

Monthly charges also showed a relationship with customer churn. The distribution of charges differed between customers who churned and customers who remained.

### 5. Payment Method

Churn also varied across payment methods, suggesting that payment behavior may provide useful information when identifying customers at greater risk of leaving.


# Task 2: Predictive Model Building

## Objective

The objective of Task 2 was to develop machine learning classification models capable of predicting whether a customer will churn.

The target variable was converted into binary form:

- `0` = No Churn
- `1` = Churn


## Data Preparation

The dataset was divided into:

- **80% training data**
- **20% testing data**

Stratified sampling was used to maintain approximately the same churn distribution in the training and testing datasets.

Categorical features were transformed using **One-Hot Encoding**, while numerical features were standardized where appropriate.


## Machine Learning Models

Two classification models were evaluated:

1. Logistic Regression
2. Random Forest Classifier


## Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score

The following results were obtained on the test dataset:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.806 | 0.657 | 0.559 | 0.604 |
| Random Forest | 0.784 | 0.621 | 0.473 | 0.537 |


## Model Comparison

Logistic Regression produced the strongest overall performance among the two models.

It achieved:

- **Accuracy:** 80.6%
- **Precision:** 65.7%
- **Recall:** 55.9%
- **F1-score:** 60.4%

Random Forest achieved:

- **Accuracy:** 78.4%
- **Precision:** 62.1%
- **Recall:** 47.3%
- **F1-score:** 53.7%

Logistic Regression outperformed Random Forest across all four reported evaluation metrics.

Recall is particularly important in a churn prediction problem because it measures how effectively the model identifies customers who actually churned.

Based on the evaluation results, **Logistic Regression was selected as the better-performing model** among the two models tested.


## Feature Influence

Logistic Regression coefficients were analyzed to investigate the features contributing most strongly to churn predictions.

The analysis showed that variables related to areas such as:

- Contract type
- Customer tenure
- Internet service
- Payment method
- Monthly charges
- Customer services

contribute useful information to churn predictions.

Positive model coefficients are associated with increased predicted churn probability, while negative coefficients are associated with decreased predicted churn probability.

These results represent **predictive associations and should not be interpreted as evidence of causation**.


# Task 3: Interactive Insights Dashboard

## Objective

The objective of Task 3 was to create an interactive dashboard allowing users to explore customer churn patterns without manually analyzing the underlying dataset.

The dashboard was developed using **Plotly and Dash**.


## Dashboard KPIs

The dashboard displays four main key performance indicators:

- Total Customers
- Churned Customers
- Churn Rate
- Average Monthly Charge


## Dashboard Visualizations

The dashboard contains multiple visualization types, including:

1. **Donut Chart** – Customer churn distribution
2. **Bar Chart** – Churn by contract type
3. **Histogram** – Monthly charges distribution
4. **Scatter Plot** – Customer tenure versus monthly charges


## Interactive Features

Users can interact with the dashboard using filters for:

- Contract Type
- Internet Service

When a filter is selected, the dashboard automatically updates the KPI values and visualizations.

Plotly also provides additional interactive functionality such as:

- Hover information
- Zooming
- Chart selection
- Legend controls


# Technologies Used

The following technologies and Python libraries were used:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Plotly
- Dash
- Google Colab
- Git
- GitHub


# Repository Structure

```text
DTEN_Customer_Churn_Analysis/
│
├── Telco_Customer_Churn_Analysis.ipynb
├── dashboard.py
├── requirements.txt
└── README.md

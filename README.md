# Telco Customer Churn Analysis & Prediction

## Project Overview

This project was completed as part of the **Data Science & Analytics Internship at Daryl Tech & Educational Network (DTEN)**.

The project analyzes telecommunications customer churn using exploratory data analysis, machine learning, and interactive data visualization.

The main objectives were to:

- Clean and explore customer data.
- Identify meaningful patterns and trends associated with customer churn.
- Develop machine learning models to predict customer churn.
- Evaluate and compare predictive models.
- Identify influential features associated with churn predictions.
- Develop and deploy an interactive dashboard for exploring customer churn.

All three DTEN Data Science & Analytics tasks were completed:

1. **Task 1:** Exploratory Data Analysis
2. **Task 2:** Predictive Model Building
3. **Task 3:** Interactive Insights Dashboard


## Live Interactive Dashboard

The completed interactive dashboard has been deployed online using Render.

### [Open the Live Customer Churn Dashboard](https://dten-customer-churn-analysis.onrender.com/)

The dashboard allows users to interactively explore customer churn using contract type and internet service filters.


## Dataset

This project uses the **Telco Customer Churn** dataset.

The dataset contains **7,043 customer records** and includes information about:

- Customer demographics
- Customer tenure
- Contract type
- Internet service
- Payment method
- Monthly charges
- Total charges
- Additional telecommunications services
- Customer churn status

The target variable is `Churn`, which indicates whether a customer left the telecommunications company.

Dataset source:

https://github.com/IBM/telco-customer-churn-on-icp4d


# Task 1: Exploratory Data Analysis

## Objective

The objective of Task 1 was to clean and analyze the dataset and identify meaningful patterns, trends, and relationships associated with customer churn.


## Data Cleaning

The following preprocessing steps were performed:

- Examined the dataset structure and data types.
- Checked for missing values.
- Checked for duplicate observations.
- Converted `TotalCharges` to numeric format.
- Handled missing `TotalCharges` values.
- Created a binary churn variable for analysis and modeling.
- Removed customer ID from the predictive modeling data.


## Exploratory Data Analysis

The exploratory analysis investigated the relationship between churn and several customer characteristics, including:

- Contract type
- Customer tenure
- Internet service
- Monthly charges
- Total charges
- Payment method
- Customer services

Visualizations were produced using **Matplotlib** and **Seaborn**.


## Key Findings

### 1. Contract Type

Customers using month-to-month contracts showed substantially higher churn than customers on longer-term contracts.

Customers with one-year and two-year contracts showed considerably lower churn.

### 2. Customer Tenure

Customers with shorter tenure showed a greater tendency to churn.

Customers who remained with the company for longer periods generally demonstrated lower churn.

### 3. Internet Service

Churn varied across internet service categories. Fiber optic customers displayed noticeably different churn behavior compared with customers using DSL or no internet service.

### 4. Monthly Charges

The distribution of monthly charges differed between customers who churned and those who remained with the company.

### 5. Payment Method

Churn also differed across payment methods, indicating that payment characteristics may provide useful predictive information.


# Task 2: Predictive Model Building

## Objective

The objective of Task 2 was to build machine learning classification models capable of predicting whether a telecommunications customer is likely to churn.

The target variable was represented as:

- `0` = No Churn
- `1` = Churn


## Data Preparation

The dataset was divided into:

- **80% training data**
- **20% testing data**

Stratified sampling was used to maintain the churn distribution across the training and test sets.

Categorical features were transformed using **One-Hot Encoding**, while numerical variables were standardized where appropriate.


## Machine Learning Models

Two classification algorithms were evaluated:

1. Logistic Regression
2. Random Forest Classifier


## Model Evaluation

Performance was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score

The models produced the following results on the held-out test set:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.806 | 0.657 | 0.559 | 0.604 |
| Random Forest | 0.784 | 0.621 | 0.473 | 0.537 |


## Model Comparison

### Logistic Regression

- **Accuracy:** 80.6%
- **Precision:** 65.7%
- **Recall:** 55.9%
- **F1-score:** 60.4%

### Random Forest

- **Accuracy:** 78.4%
- **Precision:** 62.1%
- **Recall:** 47.3%
- **F1-score:** 53.7%

Logistic Regression performed better than Random Forest across all four reported evaluation metrics.

The higher recall achieved by Logistic Regression is particularly relevant to churn prediction because recall measures the proportion of actual churned customers correctly identified by the model.

Based on these test results, **Logistic Regression was the better-performing model of the two evaluated**.


## Feature Influence

Logistic Regression coefficients were examined to understand which variables contributed strongly to churn predictions.

Features related to areas such as the following provided useful predictive information:

- Contract type
- Customer tenure
- Internet service
- Payment method
- Monthly charges
- Customer service subscriptions

Positive Logistic Regression coefficients were associated with a higher predicted probability of churn, while negative coefficients were associated with a lower predicted probability.

These relationships represent **predictive associations rather than evidence of causation**.


# Task 3: Interactive Insights Dashboard

## Objective

The objective of Task 3 was to build an interactive dashboard that allows users to visually explore customer churn patterns.

The dashboard was developed using **Plotly Dash** and deployed using **Render**.


## Dashboard KPIs

The dashboard displays four key performance indicators:

- Total Customers
- Churned Customers
- Churn Rate
- Average Monthly Charge

For the complete unfiltered dataset, the dashboard shows:

- **Total Customers:** 7,043
- **Churned Customers:** 1,869
- **Overall Churn Rate:** 26.5%
- **Average Monthly Charge:** $64.76


## Dashboard Visualizations

The dashboard contains multiple visualization types:

1. **Donut Chart** — Customer churn distribution
2. **Grouped Bar Chart** — Customer churn by contract type
3. **Histogram** — Monthly charges distribution
4. **Scatter Plot** — Customer tenure versus monthly charges


## Interactive Features

The dashboard allows users to filter the customer population by:

- **Contract Type**
- **Internet Service**

The KPI values and visualizations automatically update when filters are changed.

The Plotly visualizations also support:

- Hover information
- Zooming
- Legend interaction
- Chart exploration


## Live Dashboard

The dashboard is publicly accessible at:

**https://dten-customer-churn-analysis.onrender.com/**

> Note: Depending on the hosting plan and service activity, the dashboard may occasionally require additional time to load after a period of inactivity.


# Technologies Used

The project was developed using:

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
- Gunicorn
- Render


# Repository Structure

```text
DTEN_Customer_Churn_Analysis/
│
├── Telco_Customer_Churn_Analysis.ipynb
├── dashboard.py
├── requirements.txt
└── README.md

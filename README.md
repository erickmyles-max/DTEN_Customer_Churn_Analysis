# Telco Customer Churn Analysis and Prediction

## Project Overview

This project was completed as part of the DTEN Data Science & Analytics Internship.

The project analyzes telecommunications customer churn, identifies important patterns, develops machine learning models for churn prediction, and provides an interactive dashboard for exploring customer behavior.

## Tasks Completed

### Task 1: Exploratory Data Analysis

The Telco Customer Churn dataset was cleaned and analyzed using Pandas, Matplotlib, and Seaborn.

The analysis explored:

- Customer churn distribution
- Contract types and churn
- Customer tenure
- Internet service
- Monthly charges
- Payment methods

Several patterns associated with customer churn were identified and visualized.

### Task 2: Predictive Model Building

Two machine learning classification models were developed:

- Logistic Regression
- Random Forest

The dataset was divided into training and testing sets.

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Feature influence was also investigated to understand which customer characteristics contributed most strongly to churn predictions.

### Task 3: Interactive Dashboard

An interactive dashboard was developed using Plotly Dash.

The dashboard includes:

- KPI cards
- Churn distribution
- Churn by contract type
- Monthly charges distribution
- Tenure vs monthly charges
- Contract type filter
- Internet service filter

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Plotly
- Dash
- Google Colab

## Project Files

- `Telco_Customer_Churn_Analysis.ipynb` - complete data analysis and machine learning workflow
- `dashboard.py` - interactive Plotly Dash application
- `requirements.txt` - required Python libraries

## How to Run the Dashboard

Install the required libraries:

    pip install -r requirements.txt

Run:

    python dashboard.py

Then open the local URL displayed in the terminal.

## Limitations

The dataset represents a particular telecommunications customer sample and may not generalize to every telecommunications market.

The churn classes are also imbalanced, and potentially useful variables such as customer satisfaction, geographic information, service outages, and competitor pricing are not included.

The relationships identified should therefore be interpreted as predictive associations rather than evidence of causation.

## Internship

Data Science & Analytics Internship  
Daryl Tech & Educational Network (DTEN)

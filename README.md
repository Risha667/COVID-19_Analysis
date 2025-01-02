COVID-19 Data Insights Project
Table of Contents
Project Overview
Datasets Used
Data Cleaning
-Columns Removed
-Cleaning Steps
Data Merging
Exploratory Data Analysis (EDA)
Visualizations
Predictive Modeling
Model Evaluation
Visualizations
Recommendations

--------------------------------------------------------------------------------
Project Overview
This project utilizes the Johns Hopkins COVID-19 Dataset and additional data 
sources to analyze COVID-19 trends in infections, vaccinations, and behavioral 
factors. It involves data cleaning, merging, exploratory analysis, and 
predictive modeling to derive actionable insights.

--------------------------------------------------------------------------------
Datasets Used
COVID Burden, Behaviors, and Testing
COVID Vaccination Data
COVID Cases and Deaths
COVID Case Fatality Ratios

--------------------------------------------------------------------------------
Data Cleaning

Columns Removed
For all dataset, unnecessary or redundant columns were dropped:
-flag: Had no values.
-ci_lb, ci_ub: Confidence intervals not relevant for analysis.
-se: Standard error had no values.
-update, dataset_id: Metadata not required for analysis.

Cleaning Steps
-Converted the date column into a standard datetime format.
-Filled missing values in numeric columns with 0 and categorical columns 
with Unknown.
-Removed duplicate rows across all datasets.
-Verified consistency of key columns (country_code and date).

--------------------------------------------------------------------------------
Data Merging
-The cleaned datasets were merged on country_code and date.
-An outer join ensured no data was lost during merging.
-The merged dataset contained only the required features:
Key Columns: date, country_code, estimate_cases, estimate_vax, estimate_bbt.

--------------------------------------------------------------------------------
Exploratory Data Analysis
Visualizations
1. Infection Rates Over Time
Shows how infection rates varied over the pandemic timeline.
[Image: Infection_Rates_Over_Time.png]

2. Correlation Matrix
Explores relationships between infection rates, vaccination rates, and behavioral factors.
[Image: Correlation_matrix.png]

3. Distribution of Residuals
Evaluates the residual errors from predictive modeling.
[Image: Distribution_of_Residuals.png]

--------------------------------------------------------------------------------
Predictive Modeling

-Model Used: Random Forest Regressor
Features:
estimate_bbt: Behavioral factors.
estimate_vax: Vaccination rates.
lag_1, lag_2: Lagged infection rates.

-Target Variable: estimate_cases

-Model Evaluation:
Mean Squared Error: 3342.8696
Feature importance plot showed that lagged infection rates had the most 
predictive power.
[Image: Feature_importance.png]

-Visualizations
Actual vs Predicted Values
Scatter plot comparing predicted infection rates with actual rates.
[Image: Actual_vs_Predicted.png]

--------------------------------------------------------------------------------
Recommendations

# Public Health Recommendations:
Focus vaccination campaigns on regions with low coverage to reduce infection 
rates.
Reinforce behavioral interventions like mask-wearing and social distancing 
during outbreaks.

# Modeling Improvements:
Include external factors like population density or healthcare availability to 
refine predictions.
Explore advanced time-series models for better forecasting.

import pandas as pd

# Load datasets
burden_data = pd.read_excel('COVID_Burden_Behaviours_Testing.xlsx')
fatality_data = pd.read_excel('COVID_Case_Fatality_Ratios.xlsx')
cases_data = pd.read_excel('COVID_Cases_Deaths.xlsx')
vaccine_data = pd.read_excel('COVID_Vaccination_Data.xlsx')

# Print basic info about the datasets
print("Burden Data Info:")
print(burden_data.info())

print("\nFatality Data Info:")
print(fatality_data.info())

print("\nCases Data Info:")
print(cases_data.info())

print("\nVaccine Data Info:")
print(vaccine_data.info())

# Load datasets
burden_data = pd.read_excel('COVID_Burden_Behaviours_Testing.xlsx')
vaccine_data = pd.read_excel('COVID_Vaccination_Data.xlsx')
fatality_data = pd.read_excel('COVID_Case_Fatality_Ratios.xlsx')
cases_data = pd.read_excel('COVID_Cases_Deaths.xlsx')

# Function to clean datasets
def clean_data(df):
    # Drop unnecessary columns
    df = df.drop(['flag', 'se', 'ci_lb', 'ci_ub'], axis=1, errors='ignore')
    # Fill missing values
    df = df.fillna(0)
    # Convert 'date' to datetime
    df['date'] = pd.to_datetime(df['date'])
    return df

# Clean all datasets
burden_data = clean_data(burden_data)
vaccine_data = clean_data(vaccine_data)
fatality_data = clean_data(fatality_data)
cases_data = clean_data(cases_data)

# Save cleaned datasets
burden_data.to_csv('Cleaned_Burden_Behaviours_Testing.csv', index=False)
vaccine_data.to_csv('Cleaned_Vaccination_Data.csv', index=False)
fatality_data.to_csv('Cleaned_Case_Fatality_Ratios.csv', index=False)
cases_data.to_csv('Cleaned_Cases_Deaths.csv', index=False)

print("All datasets cleaned and saved successfully!")

import pandas as pd

# Load cleaned datasets
burden_data = pd.read_csv('Cleaned_Burden_Behaviours_Testing.csv')
vaccine_data = pd.read_csv('Cleaned_Vaccination_Data.csv')
fatality_data = pd.read_csv('Cleaned_Case_Fatality_Ratios.csv')
cases_data = pd.read_csv('Cleaned_Cases_Deaths.csv')

# Merge datasets
merged_data = pd.merge(burden_data, vaccine_data, on=['date', 'country_code', 'indicator'], how='outer', suffixes=('_bbt', '_vax'))
merged_data = pd.merge(merged_data, fatality_data, on=['date', 'country_code', 'indicator'], how='outer', suffixes=('', '_cfr'))
merged_data = pd.merge(merged_data, cases_data, on=['date', 'country_code', 'indicator'], how='outer', suffixes=('', '_cases'))

# Save merged dataset
merged_data.to_csv('Merged_COVID_Data.csv', index=False)

print("Datasets merged and saved successfully!")

print(merged_data.info())
print(merged_data.head())

print(merged_data['indicator'].unique())
print(merged_data['country_code'].unique())

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(merged_data['date'], merged_data['estimate_cases'], label='Infection Rates')
plt.xlabel('Date')
plt.ylabel('Infection Rate')
plt.title('Infection Rates Over Time')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(merged_data['estimate_vax'], merged_data['estimate_cases'], alpha=0.5)
plt.xlabel('Vaccination Rate')
plt.ylabel('Infection Rate')
plt.title('Vaccination vs Infection Rates')
plt.show()

import seaborn as sns
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

merged_data.to_csv('Processed_Merged_COVID_Data.csv', index=False)

data = merged_data[['date', 'country_code', 'estimate_cases', 'estimate_vax', 'estimate_bbt']]
data = merged_data[['date', 'country_code', 'estimate_cases', 'estimate_vax', 'estimate_bbt']]
data['date'] = pd.to_datetime(data['date'])
data = data.set_index('date')
country_data = data[data['country_code'] == 'USA']

from statsmodels.tsa.arima.model import ARIMA

# Create and fit ARIMA model
model = ARIMA(data['estimate_cases'], order=(5, 1, 0))  # Adjust (p, d, q)
model_fit = model.fit()

# Forecast future values
forecast = model_fit.forecast(steps=30)  # Predict next 30 time steps
print(forecast)


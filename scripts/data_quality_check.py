import pandas as pd
import os

# Define the directory where your CSV files are located
directory = 'C:\\Users\\User\\Desktop\\10Acadamy\\data'

# List to hold DataFrames
dataframes = []

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Build the full file path
        file_path = os.path.join(directory, filename)
       
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path, encoding='utf-8')
       
        # Add a new column with the filename
        df['source_file'] = filename
       
        # Append the DataFrame to the list
        dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('C:/Users/User/Desktop/10Acadamy/Merged_data/merged_file.csv', index=False, encoding='utf-8')

# Data Quality Check

# 1. Missing Values
print("\nMissing Values Check:")
missing_values = merged_df.isnull().sum()
print(missing_values[missing_values > 0])

# 2. Incorrect Entries
print("\nIncorrect Entries Check:")
incorrect_entries = {}
positive_columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
for col in positive_columns:
    if col in merged_df.columns:
        incorrect_entries[col] = merged_df[merged_df[col] < 0].shape[0]

print("Number of incorrect entries (negative values):")
for col, count in incorrect_entries.items():
    print(f"{col}: {count} entries")

# 3. Outlier Detection
print("\nOutlier Detection:")
def detect_outliers(df, column):
    if column in df.columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        return outliers
    else:
        return pd.DataFrame()

sensor_columns = ['ModA', 'ModB']
wind_speed_columns = ['WS', 'WSgust']

print("\nOutliers in Sensor Readings:")
for col in sensor_columns:
    outliers = detect_outliers(merged_df, col)
    print(f"\n{col}: {outliers.shape[0]} outliers detected")
    if not outliers.empty:
        print(outliers[[col]].head())

print("\nOutliers in Wind Speed Data:")
for col in wind_speed_columns:
    outliers = detect_outliers(merged_df, col)
    print(f"\n{col}: {outliers.shape[0]} outliers detected")
    if not outliers.empty:
        print(outliers[[col]].head())
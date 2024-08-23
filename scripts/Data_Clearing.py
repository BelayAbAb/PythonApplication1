# -*- coding: utf-8 -*-
import pandas as pd
import os

# Define the directory where your CSV files are located
directory = 'C:\\Users\\User\\Desktop\\10Acadamy\\data'

# Define the directory for saving plots
plot_directory = 'C:/Users/User/Desktop/10Acadamy/Plots/'

# Create the plot directory if it does not exist
if not os.path.exists(plot_directory):
    os.makedirs(plot_directory)

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

# Convert 'Timestamp' to datetime format
merged_df['Timestamp'] = pd.to_datetime(merged_df['Timestamp'], format='%Y-%m-%d %H:%M')
merged_df.set_index('Timestamp', inplace=True)

# Data Cleaning
# Drop columns that are entirely null, such as 'Comments'
merged_df.dropna(axis=1, how='all', inplace=True)

# Fill missing values in numeric columns with the mean (or another appropriate value)
numeric_columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb', 'RH', 'WS', 'WSgust', 'WSstdev', 'WD', 'WDstdev', 'BP']
for column in numeric_columns:
    if column in merged_df.columns:
        merged_df[column].fillna(merged_df[column].mean(), inplace=True)

# Handle anomalies: example for negative values in columns that should be positive
positive_columns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust', 'BP']
for column in positive_columns:
    if column in merged_df.columns:
        merged_df[column] = merged_df[column].clip(lower=0)  # Replace negative values with 0

# Optionally, remove rows with excessive missing values
threshold = 0.5 * len(merged_df.columns)  # Example: remove rows with more than 50% missing values
merged_df.dropna(thresh=threshold, inplace=True)

# Print cleaned DataFrame information
print("Cleaned DataFrame information:")
print(merged_df.info())

# Save the cleaned DataFrame to a new CSV file
cleaned_file_path = 'C:/Users/User/Desktop/10Acadamy/Merged_data/cleaned_file.csv'
merged_df.to_csv(cleaned_file_path, index=False, encoding='utf-8')

print(f"Cleaned DataFrame saved to {cleaned_file_path}")
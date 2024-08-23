# -*- coding: utf-8 -*-
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

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

# Print the first few rows of the merged DataFrame
print("First few rows of the merged DataFrame:")
print(merged_df.head())

# Convert 'Timestamp' to datetime format
merged_df['Timestamp'] = pd.to_datetime(merged_df['Timestamp'], format='%Y-%m-%d %H:%M')
merged_df.set_index('Timestamp', inplace=True)

# Ensure no duplicate indices
merged_df = merged_df.loc[~merged_df.index.duplicated(keep='first')]

# Z-Score Analysis: Calculate Z-scores for variables
variables = ['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'TModA', 'TModB']

z_scores_df = pd.DataFrame(index=merged_df.index)

for var in variables:
    if var in merged_df.columns:
        # Drop NaN values for Z-score calculation
        data = merged_df[var].dropna()
       
        # Calculate Z-scores
        z_scores = stats.zscore(data)
       
        # Add Z-scores to the DataFrame
        z_scores_df[var + '_zscore'] = np.nan  # Initialize column with NaN
        z_scores_df.loc[data.index, var + '_zscore'] = z_scores
       
        # Identify outliers (Z-score > 3 or < -3)
        outliers = z_scores_df[(z_scores_df[var + '_zscore'].abs() > 3)]
       
        # Plot histogram of Z-scores
        plt.figure(figsize=(10, 6))
        plt.hist(z_scores_df[var + '_zscore'].dropna(), bins=30, edgecolor='k', alpha=0.7)
        plt.title(f'Histogram of Z-scores for {var}')
        plt.xlabel('Z-score')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(plot_directory, f'zscore_histogram_{var}.png'))
        plt.show()
       
        print(f"Outliers in {var} (Z-score > 3 or < -3):")
        print(outliers)
    else:
        print(f"Column {var} not found in the DataFrame.")
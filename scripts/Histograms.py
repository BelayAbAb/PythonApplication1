# -*- coding: utf-8 -*-
import pandas as pd
import os
import matplotlib.pyplot as plt

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

# Histograms: Create histograms for GHI, DNI, DHI, WS, and temperatures
variables = ['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'TModA', 'TModB']

for var in variables:
    if var in merged_df.columns:
        plt.figure(figsize=(10, 6))
        plt.hist(merged_df[var].dropna(), bins=30, edgecolor='k', alpha=0.7)
        plt.title(f'Histogram of {var}')
        plt.xlabel(var)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(plot_directory, f'histogram_{var}.png'))
        plt.show()
    else:
        print(f"Column {var} not found in the DataFrame.")
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

# Bubble Chart Analysis
# Create a DataFrame for variables to plot
bubble_df = merged_df[['GHI', 'Tamb', 'RH', 'BP']].dropna()

# Plot bubble chart for GHI vs. Tamb with bubble size representing RH
plt.figure(figsize=(12, 8))
plt.scatter(bubble_df['GHI'], bubble_df['Tamb'],
            s=bubble_df['RH']*10,  # Bubble size, scaled for better visualization
            alpha=0.5,
            c=bubble_df['BP'],  # Color by BP (Barometric Pressure)
            cmap='viridis',
            edgecolors='w',
            linewidth=0.5)
plt.colorbar(label='Barometric Pressure (BP)')
plt.title('Bubble Chart: GHI vs Tamb with Bubble Size Representing RH')
plt.xlabel('Global Horizontal Irradiance (GHI)')
plt.ylabel('Ambient Temperature (Tamb)')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plot_directory, 'bubble_chart_GHI_Tamb_RH_BP.png'))
plt.show()

# Optionally, you can create additional bubble charts with different variables
# Example: Bubble chart with BP as bubble size and RH as color
plt.figure(figsize=(12, 8))
plt.scatter(bubble_df['GHI'], bubble_df['Tamb'],
            s=bubble_df['BP']*10,  # Bubble size, scaled for better visualization
            alpha=0.5,
            c=bubble_df['RH'],  # Color by RH (Relative Humidity)
            cmap='plasma',
            edgecolors='w',
            linewidth=0.5)
plt.colorbar(label='Relative Humidity (RH)')
plt.title('Bubble Chart: GHI vs Tamb with Bubble Size Representing BP')
plt.xlabel('Global Horizontal Irradiance (GHI)')
plt.ylabel('Ambient Temperature (Tamb)')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plot_directory, 'bubble_chart_GHI_Tamb_BP_RH.png'))
plt.show()
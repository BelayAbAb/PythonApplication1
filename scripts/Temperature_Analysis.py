# -*- coding: utf-8 -*-
import pandas as pd
import os
import seaborn as sns
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

# Correlation Analysis: Relative Humidity and Temperature/Solar Radiation
# Create a DataFrame for RH and temperature/solar radiation measures
analysis_df = merged_df[['RH', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI']].dropna()

# Compute the correlation matrix
corr_analysis = analysis_df.corr()

# Plot heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(corr_analysis, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap: Relative Humidity and Temperature/Solar Radiation')
plt.savefig(os.path.join(plot_directory, 'rh_temperature_solar_correlation_heatmap.png'))
plt.show()

# Scatter Plots: RH vs Temperature and Solar Radiation
plt.figure(figsize=(14, 10))

# RH vs TModA
plt.subplot(2, 2, 1)
plt.scatter(analysis_df['RH'], analysis_df['TModA'], alpha=0.5, c='blue', edgecolors='w')
plt.title('Relative Humidity vs TModA')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature TModA (\u00B0C)')
plt.grid(True)

# RH vs TModB
plt.subplot(2, 2, 2)
plt.scatter(analysis_df['RH'], analysis_df['TModB'], alpha=0.5, c='green', edgecolors='w')
plt.title('Relative Humidity vs TModB')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature TModB (\u00B0C)')
plt.grid(True)

# RH vs GHI
plt.subplot(2, 2, 3)
plt.scatter(analysis_df['RH'], analysis_df['GHI'], alpha=0.5, c='orange', edgecolors='w')
plt.title('Relative Humidity vs GHI')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Global Horizontal Irradiance (GHI)')
plt.grid(True)

# RH vs DNI
plt.subplot(2, 2, 4)
plt.scatter(analysis_df['RH'], analysis_df['DNI'], alpha=0.5, c='red', edgecolors='w')
plt.title('Relative Humidity vs DNI')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Direct Normal Irradiance (DNI)')
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig(os.path.join(plot_directory, 'rh_temperature_solar_scatter.png'))
plt.show()
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

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

# Print the first few rows of the merged DataFrame
print("First few rows of the merged DataFrame:")
print(merged_df.head())

# Convert 'Timestamp' to datetime format
merged_df['Timestamp'] = pd.to_datetime(merged_df['Timestamp'], format='%Y-%m-%d %H:%M')
merged_df.set_index('Timestamp', inplace=True)

# Wind Analysis: Polar Plot
# Prepare wind direction and speed data
wind_df = merged_df[['WD', 'WS']].dropna()

# Convert wind direction to radians for polar plot
wind_df['WD_rad'] = np.deg2rad(wind_df['WD'])

# Create a polar plot for wind direction and speed
plt.figure(figsize=(12, 8))
ax = plt.subplot(111, projection='polar')

# Plot wind speed as a function of wind direction
sc = ax.scatter(wind_df['WD_rad'], wind_df['WS'], c=wind_df['WS'], cmap='viridis', alpha=0.75, edgecolors='w', s=50)
plt.colorbar(sc, label='Wind Speed (WS)')
ax.set_title('Wind Speed Distribution and Direction')
plt.show()

# Save the polar plot
plt.savefig('C:/Users/User/Desktop/10Acadamy/Plots/wind_polar_plot.png')

# Wind Direction Variability Analysis
# Calculate wind direction standard deviation
wind_direction_std = wind_df['WD'].std()
print(f"Standard Deviation of Wind Direction: {wind_direction_std:.2f} degrees")

# Create a histogram of wind direction to visualize variability
plt.figure(figsize=(10, 6))
plt.hist(wind_df['WD'], bins=36, edgecolor='k', alpha=0.7)
plt.title('Histogram of Wind Directions')
plt.xlabel('Wind Direction (Degrees)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Save the histogram plot
plt.savefig('C:/Users/User/Desktop/10Acadamy/Plots/wind_direction_histogram.png')
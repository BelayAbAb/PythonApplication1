import pandas as pd
import os
import matplotlib.pyplot as plt

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

# Convert 'Timestamp' to datetime format
merged_df['Timestamp'] = pd.to_datetime(merged_df['Timestamp'], format='%Y-%m-%d %H:%M')

# Set 'Timestamp' as the index
merged_df.set_index('Timestamp', inplace=True)

# Plotting Time Series Data

# Create a figure for plotting
plt.figure(figsize=(14, 10))

# Plot GHI
plt.subplot(4, 1, 1)
plt.plot(merged_df.index, merged_df['GHI'], label='GHI', color='orange')
plt.title('Global Horizontal Irradiance (GHI) Over Time')
plt.xlabel('Time')
plt.ylabel('GHI')
plt.legend()
plt.grid(True)

# Plot DNI
plt.subplot(4, 1, 2)
plt.plot(merged_df.index, merged_df['DNI'], label='DNI', color='blue')
plt.title('Direct Normal Irradiance (DNI) Over Time')
plt.xlabel('Time')
plt.ylabel('DNI')
plt.legend()
plt.grid(True)

# Plot DHI
plt.subplot(4, 1, 3)
plt.plot(merged_df.index, merged_df['DHI'], label='DHI', color='green')
plt.title('Diffuse Horizontal Irradiance (DHI) Over Time')
plt.xlabel('Time')
plt.ylabel('DHI')
plt.legend()
plt.grid(True)

# Plot Tamb
plt.subplot(4, 1, 4)
plt.plot(merged_df.index, merged_df['Tamb'], label='Tamb', color='red')
plt.title('Ambient Temperature (Tamb) Over Time')
plt.xlabel('Time')
plt.ylabel('Tamb')
plt.legend()
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()
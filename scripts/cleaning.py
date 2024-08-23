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

# Plotting Sensor Readings Over Time with Cleaning Events Highlighted
plt.figure(figsize=(14, 8))

# Plot ModA
plt.subplot(2, 1, 1)
plt.plot(merged_df.index, merged_df['ModA'], label='ModA', color='blue')
plt.scatter(merged_df.index[merged_df['Cleaning'] == 1], merged_df['ModA'][merged_df['Cleaning'] == 1], color='red', label='Cleaning Event', marker='o')
plt.title('Sensor Reading ModA Over Time with Cleaning Events Highlighted')
plt.xlabel('Time')
plt.ylabel('ModA')
plt.legend()
plt.grid(True)

# Plot ModB
plt.subplot(2, 1, 2)
plt.plot(merged_df.index, merged_df['ModB'], label='ModB', color='green')
plt.scatter(merged_df.index[merged_df['Cleaning'] == 1], merged_df['ModB'][merged_df['Cleaning'] == 1], color='red', label='Cleaning Event', marker='o')
plt.title('Sensor Reading ModB Over Time with Cleaning Events Highlighted')
plt.xlabel('Time')
plt.ylabel('ModB')
plt.legend()
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()

# Save the plot
plt.savefig('C:/Users/User/Desktop/10Acadamy/Plots/sensor_readings_with_cleaning.png')
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

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

# Correlation Analysis: Heatmap
# Create a DataFrame for solar radiation and temperature measures
corr_df = merged_df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']]

# Compute the correlation matrix
corr = corr_df.corr()

# Plot heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap: Solar Radiation and Temperature Measures')
plt.show()

# Save the heatmap
plt.savefig('C:/Users/User/Desktop/10Acadamy/Plots/correlation_heatmap.png')

# Correlation Analysis: Pair Plots
# Plot pair plot for solar radiation and temperature measures
sns.pairplot(corr_df)
plt.suptitle('Pair Plot: Solar Radiation and Temperature Measures', y=1.02)
plt.show()

# Save the pair plot
plt.savefig('C:/Users/User/Desktop/10Acadamy/Plots/pair_plot_solar_temp.png')

# Scatter Matrix: Solar Irradiance and Wind Conditions
# Create a DataFrame for solar irradiance and wind conditions
scatter_matrix_df = merged_df[['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'WD']]

# Plot scatter matrix
pd.plotting.scatter_matrix(scatter_matrix_df, figsize=(12, 12), diagonal='kde')
plt.suptitle('Scatter Matrix: Solar Irradiance and Wind Conditions')
plt.show()

# Save the scatter matrix plot
plt.savefig('C:/Users/User/Desktop/10Acadamy/Plots/scatter_matrix_solar_wind.png')
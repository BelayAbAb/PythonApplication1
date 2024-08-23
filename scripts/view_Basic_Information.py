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


# Summary Statistics grouped by 'source_file'
print("\nSummary Statistics Grouped by 'source_file':")

# Group by 'source_file' and calculate summary statistics for each numeric column
grouped_stats = merged_df.groupby('source_file').describe(include='all', percentiles=[.25, .5, .75])

# Print grouped statistics
for file, stats in grouped_stats.groupby(level=0):
    print(f"\nStatistics for {file}:")
    print(stats)

# Optional: Calculate median separately if needed
median_stats = merged_df.groupby('source_file').median(numeric_only=True)
print("\nMedian Statistics for Numeric Columns Grouped by 'source_file':")
print(median_stats)
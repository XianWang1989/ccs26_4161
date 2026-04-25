
import pandas as pd
from datetime import datetime

# Start Time Counter
startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Reading the CSV file using pandas
# Use 'delimiter' to specify how to split the columns; we can combine delimiters into a regex pattern
df = pd.read_csv(data_path, delimiter='[ ;]+', header=None)

# Extract the third column (index 2), assuming it's what you want to compute pct_change on
# Convert the column to numeric, coercing errors if necessary
df[2] = pd.to_numeric(df[2], errors='coerce')

# Calculate percentage change
daily_returns = df[2].pct_change()

# Print the result or save it to a new CSV file
print(daily_returns)

# Saving daily returns to a new CSV
daily_returns.to_csv('returns.csv', index=False)

# Measure elapsed time
elapsed_time = datetime.now() - startTime
print(f"Elapsed Time: {elapsed_time}")

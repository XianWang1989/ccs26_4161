
import pandas as pd
from datetime import datetime

# Start timing
start_time = datetime.now()

# Define the path to your CSV
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using pandas
# Specify the separator as ';' and that no header row exists
# Convert the relevant column to a numeric type
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2], names=['ticks'])

# Check if the column conversion is necessary, and handle errors
df['ticks'] = pd.to_numeric(df['ticks'], errors='coerce')

# Calculate the percentage change
daily_returns = df['ticks'].pct_change()

# Print or process daily returns as needed
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# End timing and print elapsed time
print(datetime.now() - start_time)

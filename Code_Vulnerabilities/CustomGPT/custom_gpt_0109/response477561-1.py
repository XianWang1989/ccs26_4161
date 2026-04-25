
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly using pandas
# Set the appropriate delimiter and specify the columns you need
df = pd.read_csv(data_path, sep=';', usecols=[2], header=None)

# Rename the column for clarity
df.columns = ['ticks']

# Convert the column to numeric
df['ticks'] = pd.to_numeric(df['ticks'], errors='coerce')

# Compute percentage change
daily_returns = df['ticks'].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=True)

# Print execution time
print("Execution Time:", datetime.now() - start_time)


import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using Pandas, specifying the delimiter as ';'
# Set the appropriate column names or infer them from the first row if needed
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2) into a new DataFrame
# Convert it to numeric, errors='coerce' will handle any non-numeric values
ticks = pd.to_numeric(df.iloc[:, 2], errors='coerce')

# Compute the percentage change directly
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Execution time: ", datetime.now() - startTime)

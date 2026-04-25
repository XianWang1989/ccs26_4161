
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Load the CSV directly into a DataFrame
# Specify the delimiter as ';' and use whitespace as needed
df = pd.read_csv(data_path, delimiter=';', header=None, engine='python')

# Extract the third column (index 2)
ticks = df[2].astype(int)  # Convert to integers

# Calculate percentage change
daily_returns = ticks.pct_change()

# Save the results to a new CSV file
returns_path = 'returns.csv'
daily_returns.to_csv(returns_path, index=False)

print(daily_returns)
print("Processing time:", datetime.now() - startTime)


import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Use pandas to read the CSV directly
# Specify the delimiter
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2]

# Calculate the percentage change
daily_returns = ticks.pct_change()

# Save the daily returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Processing time:", datetime.now() - startTime)

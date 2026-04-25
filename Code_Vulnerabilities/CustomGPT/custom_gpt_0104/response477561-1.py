
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Use pandas to read the CSV file directly
# Specify the delimiters to appropriately parse the CSV
# Assuming your formatting generally stays the same
data = pd.read_csv(data_path, delimiter=';', header=None)

# Select the third column (index 2)
# Transform it to numeric, handling errors and coercing non-numeric values to NaN
close = pd.to_numeric(data[2], errors='coerce')

# Calculate the percentage change
daily_returns = close.pct_change(periods=1)

# Save the returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Execution time: ", datetime.now() - startTime)


import pandas as pd
from datetime import datetime

start_time = datetime.now()

path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Adjust the delimiter based on your CSV format; here we assume semicolon
df = pd.read_csv(path, sep=';', header=None)  # No header based on your provided info

# Extract the third column (index 2)
third_column = df[2]

# Calculate the percentage change
daily_returns = third_column.pct_change(periods=1)

# Print the first few daily returns for verification
print(daily_returns.head())

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

end_time = datetime.now()
print(f"Processing time: {end_time - start_time}")


import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the delimiter
deals = pd.read_csv(data_path, delimiter=';', usecols=[2], header=None)

# Calculate percentage change
daily_returns = deals.pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', header=False, index=False)

print(daily_returns)
print(f"Processing time: {datetime.now() - startTime}")

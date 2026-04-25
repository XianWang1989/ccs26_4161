
import pandas as pd
from datetime import datetime

# Start time for performance measurement
startTime = datetime.now()

# Define file path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV using pandas
# Adjust `delimiter` according to your actual file separator. Using a two-character delimiter in pandas can achieve that if necessary.
# Here, assuming semicolon (;) is the delimiter as indicated by your sample.
df = pd.read_csv(data_path, sep=';', header=None)

# Extract the third column (index 2)
close = df[2]

# Convert to a DataFrame
deals = pd.DataFrame(close)

# Calculate percentage change
daily_returns = deals.pct_change(periods=1)

# Optionally, you can take a look at the first few rows of the result
print(daily_returns.head())

# Save the results to a new CSV file
returns_path = 'returns.csv'
daily_returns.to_csv(returns_path, index=False)

# Print the duration of the operation
print("Duration: ", datetime.now() - startTime)

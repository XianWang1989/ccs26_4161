
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Specify your data path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Load the data directly into a DataFrame
# Use the correct separator for your file; here it's assumed to be a semicolon
# If the first column has some spaces, you may need to handle stripping later
df = pd.read_csv(data_path, sep=';', header=None, names=['DateTime', 'Ticker', 'Close'])

# Convert the 'Close' column (expected to be in string format) to integers
df['Close'] = df['Close'].astype(int)

# Calculate percentage change
daily_returns = df['Close'].pct_change()

# Print the resulting DataFrame with daily returns (you may choose to print only a sample)
print(daily_returns.head())

# Save to CSV
daily_returns.to_csv('returns.csv', index=False)

print(f"Processed in: {datetime.now() - startTime}")

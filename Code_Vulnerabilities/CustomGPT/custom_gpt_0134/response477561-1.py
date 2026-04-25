
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# File path
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read CSV into DataFrame directly
# Use the appropriate delimiter and specify the column names
df = pd.read_csv(data_path, delimiter=';', header=None, names=['DateTime', 'Column1', 'Close'])

# Convert the third column to numeric, coercing errors to handle non-convertible entries
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Calculate percentage change
daily_returns = df['Close'].pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print elapsed time
print(datetime.now() - startTime)


import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Use the correct separator and specify the column names
df = pd.read_csv(data_path, sep=';', header=None, names=['Date', 'ID', 'Close'])

# Calculate percentage change on the 'Close' column
daily_returns = df['Close'].pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print("Processing time:", datetime.now() - start_time)

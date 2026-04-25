
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the delimiter
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2])

# Rename the column for clarity
df.columns = ['Close']

# Compute daily percentage change
df['Pct_Change'] = df['Close'].pct_change()

# Save the result to a new CSV file
df.to_csv('returns.csv', index=False)

print("Processing time:", datetime.now() - startTime)

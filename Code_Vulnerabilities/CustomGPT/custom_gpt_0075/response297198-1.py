
import pandas as pd

# Read the CSV file with low_memory=False
data = pd.read_csv('leads.csv', low_memory=False)

# Display a sample of the data
print(data.sample(10))

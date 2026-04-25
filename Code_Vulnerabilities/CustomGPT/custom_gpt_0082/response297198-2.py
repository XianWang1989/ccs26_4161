
# Load the CSV file with low_memory option
data = pd.read_csv('leads.csv', low_memory=False)

# Optionally, check for mixed types in specific columns
print(data.info())

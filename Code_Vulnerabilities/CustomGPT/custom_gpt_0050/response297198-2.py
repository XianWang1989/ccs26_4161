
# Read CSV with low_memory option
df = pd.read_csv('leads.csv', low_memory=False)

# Check problematic columns
for col in ['col11', 'col12', 'col13', 'col14', 'col17', 'col19', 'col20', 'col21']:
    unique_types = df[col].apply(type).unique()
    print(f"Column {col} has types: {unique_types}")

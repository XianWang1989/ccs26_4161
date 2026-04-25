
# Load CSV while suppressing the DtypeWarning
df = pd.read_csv('leads.csv', low_memory=False)

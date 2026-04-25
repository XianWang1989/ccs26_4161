
import pandas as pd

# Attempt to load the CSV with error handling
try:
    # Load CSV with dtype set to str for all columns initially
    df = pd.read_csv('leads.csv', dtype=str)

    # Define a function to check for specific data type issues in the boolean column
    def identify_issues(column):
        # Check unique values and their types
        unique_values = df[column].unique()
        print(f"Unique values in {column}: {unique_values}")

    # Identify issues in the specific columns
    identify_issues('Column11')  # Replace 'Column11' with the actual name
    # Repeat for other columns with issues as needed

except pd.errors.ParserError as e:
    print("Error parsing the file:", e)

# Optionally, set low_memory=False if you require the default behavior
# df = pd.read_csv('leads.csv', low_memory=False)


import pandas as pd

# Define datatypes for specific columns
dtype_spec = {
    'column_11': 'boolean',  # Use 'bool' or 'int' if applicable
    'column_12': 'string',
    # Add the rest of your columns with their respective types
}

# Import CSV with specified dtypes
leads_df = pd.read_csv('leads.csv', dtype=dtype_spec)

# Or with low_memory=False to avoid mixed-type issues
leads_df = pd.read_csv('leads.csv', dtype=dtype_spec, low_memory=False)

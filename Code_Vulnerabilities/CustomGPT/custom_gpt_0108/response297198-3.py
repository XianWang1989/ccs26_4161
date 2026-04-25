
dtype_dict = {
    'Column11': 'bool',  # Assuming this is your Boolean column
    'Column12': 'string', # Adjust based on actual data needs
    # Add other columns as necessary
}

df = pd.read_csv(file_path, dtype=dtype_dict)

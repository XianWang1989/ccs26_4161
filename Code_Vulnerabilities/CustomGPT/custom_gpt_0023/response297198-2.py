
# Example: Check Column 11 (K) for type inconsistencies
problematic_rows = data[data.iloc[:, 11].apply(lambda x: isinstance(x, bool) or x in ['TRUE', 'FALSE'])]
print(problematic_rows)

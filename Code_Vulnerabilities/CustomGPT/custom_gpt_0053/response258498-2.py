
# Accessing column names and getting nth column value
column_names = Recipe.__table__.columns.keys()
nth_column_value = getattr(r, column_names[1])  # Replace 1 with desired index
print(nth_column_value)  # Output: Pancakes

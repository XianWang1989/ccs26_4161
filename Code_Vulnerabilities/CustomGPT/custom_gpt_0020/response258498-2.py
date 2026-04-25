
# Assuming you have the same setup above...

# Querying the recipe
r = session.query(Recipe).first()

# Accessing the nth column using __table__.columns
n = 2  # for example, to get the 'instructions'
nth_column_name = list(Recipe.__table__.columns.keys())[n]  # Get the column name
nth_value = getattr(r, nth_column_name)
print(nth_value)  # Output: Mix ingredients and cook.

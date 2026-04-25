
# Assume 'r' is an instance of Recipe
n = 2  # for example, to get the 'instructions' column

# Create a list of the columns
columns = list(Recipe.__table__.columns)

# Access the nth column value
column_value = getattr(r, columns[n].name)

print(column_value)

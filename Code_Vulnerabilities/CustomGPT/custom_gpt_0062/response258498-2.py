
# Accessing using column names
n = 2  # for example, to get 'instructions'
column_name = Recipe.__table__.columns.keys()[n]
nth_value = getattr(r, column_name)

print(f"The value of the {n}th column is: {nth_value}")

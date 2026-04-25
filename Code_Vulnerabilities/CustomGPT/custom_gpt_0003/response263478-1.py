
def foo(row, func, **kwargs):
    # Extract values from row based on the indices provided in kwargs
    row_values = {key: row[key] for key in kwargs}
    return func(**row_values, **kwargs)

def example_function(x, y, static_value):
    return x + y + static_value

# Example dataset (row)
dataset_row = {
    0: 10,
    1: 20,
    2: 30,
    3: 40
}

# Example function call
result = foo(dataset_row, example_function, x=0, y=1, static_value=5)
print(result)  # Outputs: 35 (10 + 20 + 5)

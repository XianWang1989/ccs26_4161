
def get_nth_column(instance, n):
    # Get all attribute names from the instance
    attributes = list(instance.__dict__.keys())

    # Check if the index is valid
    if n < 0 or n >= len(attributes):
        raise IndexError("Column index out of range")

    # Return the value of the nth column
    return getattr(instance, attributes[n])

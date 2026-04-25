
def get_nth_column(instance, n):
    # Make sure n is within the valid range
    if n < 0 or n >= len(instance.__table__.columns):
        raise IndexError("Column index out of range.")
    return list(instance.__dict__.values())[n]

# Example usage
nth_value = get_nth_column(r, 2)  # Get the instructions
print(nth_value)  # Output: Mix and cook on skillet.

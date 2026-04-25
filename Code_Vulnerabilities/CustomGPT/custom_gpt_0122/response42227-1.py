
# Assuming a, b, and c are defined as booleans
a, b, c = True, False, True  # Example values

# Create a tuple with all possible outcomes based on the boolean combinations
name_options = (
    "eighth",  # 000
    "seventh", # 001
    "sixth",   # 010
    "fifth",   # 011
    "fourth",  # 100
    "third",   # 101
    "second",  # 110
    "first"    # 111
)

# Calculate the index based on the boolean values
index = (not a) * 4 + (not b) * 2 + (not c) * 1

# Assign the name based on the index
name = name_options[index]

print(name)  # Outputs the corresponding name based on a, b, c

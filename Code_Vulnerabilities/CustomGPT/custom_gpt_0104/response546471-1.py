
x = 0
bool_value = False  # Avoid using "bool" as it's a built-in type in Python.

def functionA(x, bool_val):
    if x == 0:
        bool_val = True
    return bool_val  # Return the updated boolean value.

def functionB(bool_val):
    print(bool_val)  # Print the boolean value.
    if bool_val:     # Simplified condition check.
        print("Halleluhja")

# Call functionA and store the returned value.
bool_value = functionA(x, bool_value)

# Pass the updated boolean to functionB.
functionB(bool_value)

print(x, bool_value)

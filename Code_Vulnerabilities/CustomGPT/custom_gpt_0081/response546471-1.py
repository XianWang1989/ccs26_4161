
x = 0
bool_value = False  # It's a good idea to not name your variable 'bool' since it's a built-in type.

def functionA(x):
    if x == 0:
        return True  # Return True if the condition is met.
    return False  # Return False otherwise.

def functionB(bool_value):
    print(bool_value)  # Print the boolean value.
    if bool_value is True:
        print("Halleluhja")

# Get the boolean value from functionA
bool_value = functionA(x)

# Pass the returned value to functionB
functionB(bool_value)

print(x, bool_value)


x = 0
bool_value = False  # Avoid naming a variable 'bool' as it overshadows the built-in type

def functionA(x):
    if x == 0:
        return True  # Return True if condition is met
    return False  # Return False otherwise

def functionB(bool_value):
    print(bool_value)  # Use print() with parentheses in Python 3
    if bool_value:
        print("Halleluhja")

# Call functionA to get the boolean value
bool_value = functionA(x)
# Pass the returned value to functionB
functionB(bool_value)

print(x, bool_value)


x = 0
bool_value = False  # Avoid using 'bool' as a variable name as it's a built-in type

def functionA(x):
    if x == 0:  # Use '==' for comparison instead of 'is'
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Call functionA and store its return value
bool_value = functionA(x)

# Pass the updated boolean value to functionB
functionB(bool_value)

print(x, bool_value)

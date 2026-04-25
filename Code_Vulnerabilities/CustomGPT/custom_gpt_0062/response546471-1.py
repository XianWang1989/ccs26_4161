
x = 0
bool_value = False  # Use a different name to avoid conflict with the built-in 'bool'

def functionA(x):
    if x == 0:
        return True  # Return the boolean value

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Call functionA and get the boolean value
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)

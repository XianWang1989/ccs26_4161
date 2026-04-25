
x = 0
bool_value = False  # Use a different name to avoid shadowing the built-in 'bool'

def functionA(x):
    return x == 0  # Return True if x is 0, else False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Call functionA and store its return value
bool_value = functionA(x)
# Pass the updated boolean value to functionB
functionB(bool_value)

print(x, bool_value)


x = 0

def functionA(x):
    return x == 0  # Return True if x is 0, otherwise False

def functionB(bool_val):
    print(bool_val)
    if bool_val:
        print("Halleluhja")

# Call functionA and get the boolean value
bool_value = functionA(x)

# Pass the boolean value to functionB
functionB(bool_value)

print(x, bool_value)


x = 0
bool_val = False  # Renamed to avoid overriding the built-in bool type

def functionA(x):
    if x == 0:
        return True  # Return the updated boolean value
    return False

def functionB(bool_val):
    print(bool_val)
    if bool_val:
        print("Halleluhja")

# Get the boolean value from functionA
bool_val = functionA(x)
functionB(bool_val)

print(x, bool_val)

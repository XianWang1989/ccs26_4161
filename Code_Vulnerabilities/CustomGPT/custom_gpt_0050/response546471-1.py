
x = 0
bool_value = False  # Renamed to avoid shadowing the built-in 'bool' type

def functionA(x):
    if x == 0:
        return True  # Return the updated boolean value
    return False

def functionB(bool_value):
    print(bool_value)  # Python 3 syntax
    if bool_value:
        print("Hallelujah")  # Fixed spelling

# Call functionA and store the returned value
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)

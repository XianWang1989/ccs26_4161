
x = 0
bool_value = False  # Renamed 'bool' to 'bool_value' to avoid shadowing the built-in bool type

def functionA(x, bool_value):
    if x == 0:
        return True  # Return True when condition is met
    return bool_value  # In case condition is not met, return the original bool_value

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Hallelujah")

# Call functionA and pass the return value to functionB
bool_value = functionA(x, bool_value)
functionB(bool_value)

print(x, bool_value)

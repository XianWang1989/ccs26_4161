
x = 0
bool_value = False  # Use a different name to avoid confusion with built-in `bool`

def functionA(x):
    if x == 0:
        return True  # Return the new boolean value
    return False  # Return False if the condition is not met

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Call functionA and capture the returned boolean
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)  # Prints the current value of x and bool_value

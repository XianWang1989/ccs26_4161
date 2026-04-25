
x = 0

def functionA(x):
    bool_value = False  # Rename to avoid using built-in name
    if x == 0:
        bool_value = True
    return bool_value  # Return the boolean value

def functionB(bool_value):
    print(bool_value)  # Use print function for compatibility
    if bool_value is True:
        print("Hallelujah")  # Fixed the spelling of Hallelujah

bool_value = functionA(x)  # Capture the return value
functionB(bool_value)  # Pass the returned value

print(x, bool_value)  # Print updated values

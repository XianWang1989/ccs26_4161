
x = 0
bool_value = False

def functionA(x):
    if x == 0:
        return True  # Return True when x is 0
    return False  # Return False otherwise

def functionB(bool_value):
    print(bool_value)  # Printing the boolean value
    if bool_value:
        print("Halleluhja")

# Call functionA and store the returned boolean value
bool_value = functionA(x)
# Pass the boolean value to functionB
functionB(bool_value)

print(x, bool_value)  # Need to use bool_value here

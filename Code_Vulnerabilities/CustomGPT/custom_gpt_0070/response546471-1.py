
x = 0
bool_value = False

def functionA(x):
    if x == 0:  # Use '==' for comparison
        return True
    return False

def functionB(bool_value):
    print(bool_value)  # Use parentheses for print function (Python 3)
    if bool_value is True:
        print("Hallelujah")

# Call functionA and capture its return value
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)

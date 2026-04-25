
x = 0
bool_value = False

def functionA(x, bool_value):
    if x == 0:
        bool_value = True
    return bool_value

def functionB(bool_value):
    print(bool_value)  # Use parentheses for print in Python 3
    if bool_value:
        print("Halleluhja")

# Update the boolean value from functionA
bool_value = functionA(x, bool_value)
functionB(bool_value)

print(x, bool_value)

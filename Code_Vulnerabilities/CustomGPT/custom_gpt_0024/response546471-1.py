
x = 0
bool_value = False  # Changed variable name to avoid conflict with built-in `bool`

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

bool_value = functionA(x)  # Call functionA and assign the result to bool_value
functionB(bool_value)

print(x, bool_value)

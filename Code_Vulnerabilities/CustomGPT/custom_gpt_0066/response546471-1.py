
x = 0
bool_value = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

bool_value = functionA(x)  # Get the boolean from functionA
functionB(bool_value)  # Pass the boolean to functionB

print(x, bool_value)

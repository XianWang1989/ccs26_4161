
x = 0
bool_value = False  # Changed from 'bool' to 'bool_value' to avoid shadowing

def functionA(x, bool_value):
    if x == 0:
        bool_value = True
    return bool_value

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Halleluhja")

bool_value = functionA(x, bool_value)  # Update bool_value with the returned value
functionB(bool_value)

print(x, bool_value)

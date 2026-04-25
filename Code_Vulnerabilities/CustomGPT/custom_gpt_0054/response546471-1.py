
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

# Update the boolean variable based on functionA's return value
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)

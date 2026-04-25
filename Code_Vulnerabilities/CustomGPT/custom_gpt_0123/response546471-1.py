
x = 0

def functionA(x):
    bool_value = False
    if x == 0:
        bool_value = True
    return bool_value

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Halleluhja")

# Get the boolean value from functionA
bool_value = functionA(x)

# Pass the returned value to functionB
functionB(bool_value)

print(x, bool_value)

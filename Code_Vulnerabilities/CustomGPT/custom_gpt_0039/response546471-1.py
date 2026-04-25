
x = 0
bool_value = False

def functionA(x, bool_value):
    if x == 0:
        bool_value = True
    return bool_value

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Halleluhja")

# Update the bool_value by calling functionA
bool_value = functionA(x, bool_value)
functionB(bool_value)

print(x, bool_value)

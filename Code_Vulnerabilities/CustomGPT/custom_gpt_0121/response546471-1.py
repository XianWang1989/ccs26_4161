
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Halleluhja")

bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)

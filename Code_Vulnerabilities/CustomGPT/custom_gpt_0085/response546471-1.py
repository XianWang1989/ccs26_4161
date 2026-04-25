
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(flag):
    print(flag)
    if flag:
        print("Halleluhja")

# Get the boolean from functionA
bool_value = functionA(x)
# Pass the boolean to functionB
functionB(bool_value)

print(x, bool_value)

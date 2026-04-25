
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(flag):
    print(flag)
    if flag:
        print("Halleluhja")

# Call functionA and get the boolean value
bool_value = functionA(x)
# Pass the boolean value to functionB
functionB(bool_value)

print(x, bool_value)

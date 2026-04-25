
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(flag):
    print(flag)
    if flag is True:
        print("Hallelujah")

# Call functionA and store the returned value in the bool variable
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)

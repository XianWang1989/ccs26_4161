
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(flag):
    print(flag)
    if flag is True:
        print("Hallelujah")

# Call functionA and capture the return value
bool_value = functionA(x)
# Pass the value returned from functionA to functionB
functionB(bool_value)

print(x, bool_value)

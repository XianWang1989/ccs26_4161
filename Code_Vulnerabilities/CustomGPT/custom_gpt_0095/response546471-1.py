
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(flag):
    print(flag)
    if flag:
        print("Hallelujah")

# Call functionA and store its return value
bool_value = functionA(x)
# Pass the returned value to functionB
functionB(bool_value)

print(x, bool_value)

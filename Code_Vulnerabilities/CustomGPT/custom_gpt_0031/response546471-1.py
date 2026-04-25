
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(flag):
    print(flag)
    if flag:
        print("Hallelujah")

# Call functionA and store the result in bool
bool_result = functionA(x)

# Call functionB with the result
functionB(bool_result)

print(x, bool_result)

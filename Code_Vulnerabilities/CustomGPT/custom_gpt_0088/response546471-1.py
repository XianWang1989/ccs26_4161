
x = 0
boolean_flag = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(boolean_flag):
    print(boolean_flag)
    if boolean_flag is True:
        print("Hallelujah")

# Call functionA and store the returned value
boolean_flag = functionA(x)

# Call functionB with the updated boolean_flag
functionB(boolean_flag)

print(x, boolean_flag)

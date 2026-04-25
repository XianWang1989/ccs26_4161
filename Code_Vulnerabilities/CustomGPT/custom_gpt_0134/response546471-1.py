
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(flag):
    print(flag)
    if flag:
        print("Hallelujah")

# Call functionA and store the returned boolean
flag = functionA(x)
functionB(flag)

print(x, flag)

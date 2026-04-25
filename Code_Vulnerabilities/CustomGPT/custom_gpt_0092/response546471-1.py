
x = 0
bool_val = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_val):
    print(bool_val)
    if bool_val:
        print("Hallelujah")

# Update the boolean by calling functionA
bool_val = functionA(x)
functionB(bool_val)

print(x, bool_val)

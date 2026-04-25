
x = 0
bool_var = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_var):
    print(bool_var)
    if bool_var:
        print("Hallelujah")

# Update the boolean by calling functionA
bool_var = functionA(x)

# Pass the updated boolean to functionB
functionB(bool_var)

print(x, bool_var)

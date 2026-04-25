
x = 0

def functionA(x):
    bool_val = False
    if x == 0:
        bool_val = True
    return bool_val

def functionB(bool_val):
    print(bool_val)
    if bool_val:
        print("Hallelujah")

# Get the boolean value from functionA and pass it to functionB
bool_val = functionA(x)
functionB(bool_val)

print(x, bool_val)

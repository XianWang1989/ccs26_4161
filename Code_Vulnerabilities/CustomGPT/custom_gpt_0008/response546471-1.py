
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_var):
    print(bool_var)
    if bool_var is True:
        print("Hallelujah")

# Call functionA and capture its return value
bool_value = functionA(x)

# Pass the returned value to functionB
functionB(bool_value)

print(x, bool_value)

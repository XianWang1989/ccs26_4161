
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Hallelujah")

# Call functionA and capture the returned boolean value
bool_value = functionA(x)
# Pass the returned value to functionB
functionB(bool_value)

print(x, bool_value)

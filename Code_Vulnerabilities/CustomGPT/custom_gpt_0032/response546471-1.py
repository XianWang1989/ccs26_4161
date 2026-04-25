
x = 0
bool_value = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Call functionA to get the updated boolean value
bool_value = functionA(x)

# Pass the updated boolean value to functionB
functionB(bool_value)

print(x, bool_value)

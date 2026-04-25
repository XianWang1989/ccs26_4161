
x = 0
bool_value = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Halleluhja")

# Call functionA and store the result
bool_value = functionA(x)

# Call functionB with the updated boolean
functionB(bool_value)

print(x, bool_value)

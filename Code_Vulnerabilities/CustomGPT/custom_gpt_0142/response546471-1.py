
x = 0

def functionA(x):
    if x is 0:
        return True
    else:
        return False

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Halleluhja")

# Call functionA and store the returned boolean value
bool_value = functionA(x)

# Now pass the result to functionB
functionB(bool_value)

print(x, bool_value)

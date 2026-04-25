
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(value):
    print(value)
    if value:
        print("Halleluhja")

# Call functionA and get the boolean result
boolean_value = functionA(x)

# Pass the result to functionB
functionB(boolean_value)

print(x, boolean_value)

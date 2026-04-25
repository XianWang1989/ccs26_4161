
x = 0
boolean_value = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(boolean_value):
    print(boolean_value)
    if boolean_value:
        print("Hallelujah")

# Call functionA and get its return value
boolean_value = functionA(x)
# Call functionB with the updated boolean value
functionB(boolean_value)

print(x, boolean_value)

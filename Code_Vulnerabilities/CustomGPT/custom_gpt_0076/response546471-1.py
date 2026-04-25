
x = 0
bool_val = False

def functionA(x):
    if x == 0:
        return True  # Return the modified boolean value
    return False

def functionB(bool_val):
    print(bool_val)
    if bool_val:
        print("Halleluhja")

# Call functionA and store the result
bool_val = functionA(x)
functionB(bool_val)

print(x, bool_val)

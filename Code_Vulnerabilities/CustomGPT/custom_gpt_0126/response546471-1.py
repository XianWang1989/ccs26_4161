
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

bool_value = functionA(x)  # Call functionA and store the result
functionB(bool_value)       # Pass the result to functionB

print(x, bool_value)        # Print x and boolean value

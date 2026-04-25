
def functionA(x):
    # Return True if x is 0, otherwise return False
    return x == 0

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Update the way you call the functions:
x = 0
bool_value = functionA(x)  # Capture the return value

functionB(bool_value)

print(x, bool_value)  # Will print the current value of x and the boolean

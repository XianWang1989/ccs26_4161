
x = 0

def functionA(x):
    # Return True if x is 0
    return x == 0

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Call functionA and store the result
bool_value = functionA(x)
# Pass the result to functionB
functionB(bool_value)

print(x, bool_value)

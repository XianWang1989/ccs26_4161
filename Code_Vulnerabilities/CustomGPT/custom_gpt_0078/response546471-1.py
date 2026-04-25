
x = 0
bool_value = False

def functionA(x):
    if x == 0:
        return True  # Returns True if x is 0
    return False     # Returns False otherwise

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Call functionA and get the boolean value
bool_value = functionA(x)
# Pass the result to functionB
functionB(bool_value)

print(x, bool_value)


x = 0
bool_value = False  # Use a different name than 'bool' since it's a built-in type

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Hallelujah")

# Update the boolean value from functionA
bool_value = functionA(x)
# Use the updated boolean value in functionB
functionB(bool_value)

print(x, bool_value)


x = 0
bool_flag = False  # Avoid using 'bool' since it's a built-in type name

def functionA(x):
    if x == 0:
        return True  # Return True or False based on your condition
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Hallelujah")

# Call functionA and capture the returned value
bool_flag = functionA(x)
# Pass the updated value to functionB
functionB(bool_flag)

print(x, bool_flag)


x = 0
bool_value = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Hallelujah")

# Call functionA and get the boolean value
bool_value = functionA(x)
# Pass the updated boolean to functionB
functionB(bool_value)

print(x, bool_value)


x = 0
bool_variable = False

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_variable):
    print(bool_variable)
    if bool_variable:
        print("Halleluhja")

# Update the boolean from functionA
bool_variable = functionA(x)
# Pass the updated boolean to functionB
functionB(bool_variable)

print(x, bool_variable)

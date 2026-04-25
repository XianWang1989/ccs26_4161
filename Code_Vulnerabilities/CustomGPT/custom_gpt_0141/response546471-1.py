
x = 0

def functionA(x):
    # Initialize local variable to store boolean state
    bool_value = False
    if x == 0:
        bool_value = True
    return bool_value  # Return the modified boolean value

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Hallelujja")

# Call functionA and pass its return value to functionB
bool_result = functionA(x)
functionB(bool_result)

print(x, bool_result)

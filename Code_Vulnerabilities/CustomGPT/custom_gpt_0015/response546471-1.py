
x = 0
bool_value = False  # Changed variable name to avoid confusion with built-in

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Call functionA and store its return value
bool_value = functionA(x)
# Pass the updated boolean to functionB
functionB(bool_value)

print(x, bool_value)

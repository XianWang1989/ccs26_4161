
x = 0
bool_value = False  # Renaming 'bool' to 'bool_value' to avoid confusion with the built-in `bool`.

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Halleluhja")

# Call functionA and get the boolean value
bool_value = functionA(x)

# Call functionB with the returned boolean value
functionB(bool_value)

print(x, bool_value)

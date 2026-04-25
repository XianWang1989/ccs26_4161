
x = 0
bool_value = False  # Renamed to avoid shadowing built-in names

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Update bool_value based on the result from functionA
bool_value = functionA(x)
functionB(bool_value)

print(x, bool_value)

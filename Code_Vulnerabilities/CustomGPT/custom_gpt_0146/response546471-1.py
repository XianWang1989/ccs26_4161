
x = 0
bool_value = False  # Avoid using 'bool' as it can shadow the built-in name

def functionA(x, bool_value):
    if x == 0:
        return True  # Return the new boolean value
    return bool_value  # Return the original value if x is not 0

def functionB(bool_value):
    print(bool_value)
    if bool_value is True:
        print("Halleluhja")

# Call functionA and capture the returned boolean value
bool_value = functionA(x, bool_value)
# Pass the updated boolean value to functionB
functionB(bool_value)

print(x, bool_value)


x = 0
bool_value = False  # Renamed to avoid using 'bool', which is a built-in type

def functionA(x, bool_value):
    if x == 0:  # Use '==' for comparison, not 'is'
        bool_value = True
    return bool_value  # Return the updated value

def functionB(bool_value):
    print(bool_value)  # Use parentheses for print function
    if bool_value:
        print("Halleluhja")

# Call functionA and get the updated boolean
bool_value = functionA(x, bool_value)
# Now call functionB with the updated boolean
functionB(bool_value)

print(x, bool_value)  # Output the values

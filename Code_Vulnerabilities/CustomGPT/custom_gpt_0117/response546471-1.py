
x = 0
boolean_var = False  # Renamed 'bool' to 'boolean_var' to avoid shadowing

def functionA(x):
    if x == 0:
        return True  # Return True if conditions are met
    return False  # Return False otherwise

def functionB(boolean_var):
    print(boolean_var)  # Print the received boolean
    if boolean_var == True:
        print("Hallelujah")  # Correct spelling

# Call functionA and use its return value
boolean_var = functionA(x)  
functionB(boolean_var)  # Pass the updated boolean

print(x, boolean_var)

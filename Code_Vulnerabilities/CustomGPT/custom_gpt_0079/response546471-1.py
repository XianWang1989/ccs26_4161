
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

# Call functionA and get the boolean value
result = functionA(x)
# Pass the result to functionB
functionB(result)

print(x, result)

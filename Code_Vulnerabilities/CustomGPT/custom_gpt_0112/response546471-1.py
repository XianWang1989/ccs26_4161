
x = 0

def functionA(x):
    if x == 0:
        return True
    return False

def functionB(value):
    print(value)
    if value:
        print("Hallelujah")

# Call functionA and capture the return value
result = functionA(x)

# Pass the result to functionB
functionB(result)

print(x, result)

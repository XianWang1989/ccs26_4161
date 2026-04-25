
x = 0
bool_flag = False

def functionA(x):
    # Use a return value to get the updated boolean
    if x == 0:
        return True
    return False

def functionB(bool_flag):
    print(bool_flag)
    if bool_flag:
        print("Halleluhja")

# Call functionA and store the return value
bool_flag = functionA(x)
functionB(bool_flag)

print(x, bool_flag)

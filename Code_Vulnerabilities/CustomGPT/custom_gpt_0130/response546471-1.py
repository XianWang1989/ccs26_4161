
x = 0

def functionA(x):
    bool_value = False
    if x == 0:
        bool_value = True
    return bool_value

def functionB(bool_value):
    print(bool_value)
    if bool_value:
        print("Halleluhja")

bool_result = functionA(x)
functionB(bool_result)

print(x, bool_result)


def first_function():
    print("This is the first function.")

def second_function():
    print("This is the second function.")
    first_function()

def third_function():
    print("This is the third function.")
    second_function()

if __name__ == "__main__":
    third_function()

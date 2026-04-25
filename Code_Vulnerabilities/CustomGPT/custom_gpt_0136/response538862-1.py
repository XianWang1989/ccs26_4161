
def method_one():
    print("This is method one")

def method_two():
    print("This is method two")

def main():
    method_one()
    method_two()  # Recently accessed methods will be in context here

if __name__ == "__main__":
    main()

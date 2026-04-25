
from package import MODULE1, MODULE2, MODULE3

def main():
    name = input('Please Enter your question: ').lower()

    # Check MODULE1
    MODULE1.check_color(name)

    # Check MODULE2
    MODULE2.check_cars(name)

    # Check MODULE3
    MODULE3.check_toys(name)

if __name__ == "__main__":
    main()

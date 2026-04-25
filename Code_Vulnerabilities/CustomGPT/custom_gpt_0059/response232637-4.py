
from package import MODULE1, MODULE2, MODULE3

def main():
    name = input('Please Enter your question: ').lower()

    # Try to check with each module sequentially
    MODULE1.check_color(name)
    MODULE2.check_cars(name)
    MODULE3.check_foods(name)

if __name__ == "__main__":
    main()


# main.py
from package import MODULE1, MODULE2

def main():
    name = input('Please Enter your question: ').lower()

    # List of functions to check
    modules = [MODULE1.handle_color, MODULE2.handle_cars]  # Add other modules here

    for module in modules:
        module(name)  # Call each module with the input

if __name__ == '__main__':
    main()

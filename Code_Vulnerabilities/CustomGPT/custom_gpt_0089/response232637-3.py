
from package import MODULE1, MODULE2  # Import your modules

def main():
    name = input('Please enter your question: ').lower()

    # Try each module in order
    if len(name) >= 3:
        MODULE1.handle_input(name)
    if len(name) >= 3:
        MODULE2.handle_input(name)
    # Add more modules as needed

if __name__ == "__main__":
    main()

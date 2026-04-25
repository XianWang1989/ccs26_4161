
from package import MODULE1, MODULE2  # Import necessary modules

def main():
    name = input('Please Enter your question: ').lower()

    # Check MODULE1
    response = MODULE1.check_color(name)
    if response:
        print(response)
        return  # Exit if a response was found

    # Check MODULE2
    response = MODULE2.check_cars(name)
    if response:
        print(response)
        return  # Exit if a response was found

    print("No matches found.")

if __name__ == "__main__":
    main()

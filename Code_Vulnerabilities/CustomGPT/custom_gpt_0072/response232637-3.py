
from package import MODULE1, MODULE2

def main():
    name = input('Please enter your question: ').lower()

    response = MODULE1.check_color(name)
    if response:
        print(response)
    else:
        response = MODULE2.check_cars(name)
        if response:
            print(response)
        else:
            print("No matches found in available modules.")

if __name__ == "__main__":
    main()

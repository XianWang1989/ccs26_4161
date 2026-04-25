
from package import MODULE1, MODULE2

def main():
    user_input = input('Please enter your question: ').lower()

    # Call MODULE1 first
    MODULE1.process_input(user_input)

    # If MODULE1 didn't handle it, call MODULE2
    MODULE2.process_input(user_input) # Add more module calls as needed

if __name__ == "__main__":
    main()

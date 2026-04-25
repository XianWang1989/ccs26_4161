
# main.py
from package import MODULE1, MODULE2, MODULE3, MODULE4

def main():
    user_input = input('Please enter your question: ').lower()

    if len(user_input) >= 3:
        MODULE1.handle_input(user_input)

    if len(user_input) >= 3:  # repeat for other modules
        MODULE2.handle_input(user_input)

    if len(user_input) >= 3:
        MODULE3.handle_input(user_input)

    # Add additional checks for MODULE4 or further logic as needed

if __name__ == "__main__":
    main()

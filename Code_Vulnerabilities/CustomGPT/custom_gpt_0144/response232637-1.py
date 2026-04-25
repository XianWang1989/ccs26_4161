from package import MODULE1, MODULE2, MODULE3

def main():
    user_input = input('Please Enter your question: ').lower()

    if MODULE1.can_handle(user_input):
        MODULE1.run(user_input)
    elif MODULE2.can_handle(user_input):
        MODULE2.run(user_input)
    elif MODULE3.can_handle(user_input):
        MODULE3.run(user_input)
    else:
        print("Sorry, I couldn't understand your question.")

if __name__ == "__main__":
    main()


# Import all the necessary modules
from package import MODULE1, MODULE2, MODULE3, MODULE4

# Function to handle user input and delegate to the corresponding module
def main():
    name = input('Please Enter your question: ').lower()

    if MODULE1.check_question(name):
        MODULE1.run()
    elif MODULE2.check_question(name):
        MODULE2.run()
    elif MODULE3.check_question(name):
        MODULE3.run()
    elif MODULE4.check_question(name):
        MODULE4.run()
    else:
        print("No suitable module found for your question.")

if __name__ == '__main__':
    main()

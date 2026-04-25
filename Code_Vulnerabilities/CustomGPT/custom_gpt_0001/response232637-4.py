
from package import MODULE1, MODULE2, MODULE3

def main():
    # Get user input
    question = input('Please Enter your question: ').lower()

    # Check the question with MODULE1
    MODULE1.run_module()

    # If the user didn't find a match in MODULE1
    if 'found color' not in MODULE1.run_module():
        MODULE2.run_module()

    # If the user didn't find a match in MODULE2
    if 'found car' not in MODULE2.run_module():
        MODULE3.run_module()

if __name__ == "__main__":
    main()

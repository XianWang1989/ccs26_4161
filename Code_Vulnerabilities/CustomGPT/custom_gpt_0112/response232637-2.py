
from package import MODULE1, MODULE2, MODULE3, MODULE4  # Import specific modules

def main():
    question = input('Please Enter your question: ').lower()

    if len(question) >= 3:  # Modify the condition as needed
        MODULE1.run_module()
    if len(question) >= 6:  # Example condition for MODULE2
        MODULE2.run_module()
    if len(question) >= 9:  # Example condition for MODULE3
        MODULE3.run_module()
    # Continue with additional modules as needed

if __name__ == "__main__":
    main()

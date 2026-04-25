
# main_program.py
from package import *

def main():
    question = input('Please Enter your question: ').lower()

    # Check against the modules in order
    if MODULE1.check_condition(question):  # Assuming MODULE1 has a function named check_condition
        MODULE1.run_module1(question)
    elif MODULE2.check_condition(question):
        MODULE2.run_module2(question)
    elif MODULE3.check_condition(question):
        MODULE3.run_module3(question)
    # Add more elif statements for subsequent modules

if __name__ == "__main__":
    main()

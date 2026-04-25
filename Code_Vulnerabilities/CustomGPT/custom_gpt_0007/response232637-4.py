
from package import *

def main():
    name = input('Please Enter your question: ').lower()

    if 'color' in name:
        MODULE1.run_module1()
    elif 'car' in name:
        MODULE2.run_module2()
    elif 'toy' in name:
        MODULE3.run_module3()
    # Continue for other modules...

if __name__ == "__main__":
    main()

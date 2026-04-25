
from package import *

def main():
    question = input('Please enter your question: ').lower()

    # Add logic to determine which module to call
    if 'color' in question:
        MODULE1.run()
    elif 'cars' in question:
        MODULE2.run()
    elif 'toys' in question:
        MODULE3.run()
    else:
        print("No suitable module found.")

if __name__ == "__main__":
    main()

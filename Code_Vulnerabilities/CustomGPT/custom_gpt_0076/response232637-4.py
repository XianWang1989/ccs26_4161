
# main.py
from package import *

def main():
    name = input('Please Enter your question: ').lower()

    if MODULE1.run(name):
        return
    if MODULE2.run(name):
        return
    if MODULE3.run(name):  # Add MODULE3 and MODULE4 similarly
        return
    print("No match found in the modules.")

if __name__ == "__main__":
    main()

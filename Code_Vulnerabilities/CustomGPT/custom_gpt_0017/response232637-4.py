
from package import *

def main():
    name = input('Please Enter your question: ').lower()
    length = len(name.split())

    if length >= 3:
        MODULE1.run_module()
    if length >= 3:
        MODULE2.run_module()
    # Continue for MODULE3, MODULE4, etc.

if __name__ == "__main__":
    main()


from package import *

def main():
    name = input('Please Enter your question: ').lower()

    # Check each module in order
    for module in [MODULE1, MODULE2, MODULE3, MODULE4]:
        if hasattr(module, 'run_game'):
            module.run_game(name)  # Call the function defined in each module

if __name__ == '__main__':
    main()

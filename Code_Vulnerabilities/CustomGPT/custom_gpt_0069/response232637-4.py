
from package.MODULE1 import run_module as run_module1
from package.MODULE2 import run_module as run_module2
from package.MODULE3 import run_module as run_module3

def main():
    name = input('Please Enter your question: ').lower()

    if len(name) >= 3:
        run_module1(name)
    else:
        run_module2(name)

    # You can add more conditions to check other modules

if __name__ == "__main__":
    main()

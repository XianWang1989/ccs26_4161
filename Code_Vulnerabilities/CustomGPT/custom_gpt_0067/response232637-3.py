
from package.MODULE1 import run_module as run_module1
from package.MODULE2 import run_module as run_module2

def main():
    name = input('Please enter your question: ').lower()

    modules = [run_module1, run_module2]  # Add more module functions as needed

    for run_module in modules:
        run_module(name)

if __name__ == "__main__":
    main()

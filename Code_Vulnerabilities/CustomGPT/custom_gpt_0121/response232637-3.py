
from package.MODULE1 import run_module as run_module1
from package.MODULE2 import run_module as run_module2
# import other modules similarly...

def main():
    name = input('Please Enter your question: ').lower()

    # List of callable modules
    modules = [run_module1, run_module2]  # Add your other module functions here

    for module in modules:
        module(name)

if __name__ == "__main__":
    main()

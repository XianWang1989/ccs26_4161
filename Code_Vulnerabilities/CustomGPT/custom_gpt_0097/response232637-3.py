
from package import MODULE1, MODULE2  # Import your modules

def main():
    name = input('Please Enter your question: ').lower()

    # List of modules to check with their corresponding functions
    modules = [MODULE1, MODULE2]

    for module in modules:
        module.run()  # Call the run function of each module

if __name__ == "__main__":
    main()

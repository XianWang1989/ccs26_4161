
from package import MODULE1, MODULE2  # Import specific modules

def main():
    # List of modules to check
    modules = [MODULE1, MODULE2]

    for module in modules:
        module.run()  # Call the run function from each module

if __name__ == '__main__':
    main()

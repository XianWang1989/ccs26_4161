
from package import MODULE1, MODULE2, MODULE3

def main():
    modules = [MODULE1, MODULE2, MODULE3]

    for module in modules:
        if module.run_module():  # Call the run_module function in each module
            break  # Stop if a match is found

if __name__ == "__main__":
    main()

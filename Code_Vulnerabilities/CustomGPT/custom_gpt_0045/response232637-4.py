
from package import MODULE1, MODULE2, MODULE3

def main():
    name = input('Please Enter your question: ').lower()
    modules = [MODULE1, MODULE2, MODULE3]

    for module in modules:
        module.run_module(name)

if __name__ == "__main__":
    main()


from package import MODULE1, MODULE2

def main():
    name = input('Please enter your question: ').lower()
    if len(name) >= 3:
        MODULE1.run_module()
        MODULE2.run_module()
        # Add additional modules as needed

if __name__ == "__main__":
    main()

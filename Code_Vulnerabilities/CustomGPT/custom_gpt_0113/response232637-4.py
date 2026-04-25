
from package import module1, module2, module3

def main():
    name = input('Please Enter your question: ').lower()

    response = module1.run_module(name)
    if response:
        print(response)
    else:
        response = module2.run_module(name)
        if response:
            print(response)
        else:
            response = module3.run_module(name)
            if response:
                print(response)
            else:
                print("No matches found.")

if __name__ == "__main__":
    main()


from package import MODULE1, MODULE2, MODULE3, MODULE4

def main():
    name = input('Please enter your question: ').lower()

    # Check against the modules and run the corresponding function
    if MODULE1.run_module(name):
        return
    if MODULE2.run_module(name):
        return
    if MODULE3.run_module(name):
        return
    if MODULE4.run_module(name):
        return

    print("Sorry, I couldn't find a response for your question.")

if __name__ == "__main__":
    main()


# main.py
from package.MODULE1 import main as main_module1
from package.MODULE2 import main as main_module2
# import other modules as needed

def main():
    while True:
        user_input = input("Please enter your question: ").lower()

        if main_module1(user_input):
            break
        elif main_module2(user_input):
            break
        # Add calls for MODULE3, MODULE4, etc. similarly

if __name__ == "__main__":
    main()

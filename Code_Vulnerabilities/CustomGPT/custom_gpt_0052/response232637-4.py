
from package import *

def main():
    name = input('Please enter your question: ').lower()

    modules = [MODULE1, MODULE2, MODULE3]  # List your modules here
    for module in modules:
        result = module.play_game(name)
        if result:
            print(result)
            break
    else:
        print("No games found for your question.")

if __name__ == "__main__":
    main()

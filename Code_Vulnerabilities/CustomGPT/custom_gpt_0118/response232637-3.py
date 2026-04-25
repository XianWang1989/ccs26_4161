
from package import MODULE1, MODULE2

def main():
    name = input('Please Enter your question: ').lower()

    # Check MODULE1 first
    MODULE1.run_game(name)

    # If you want to check MODULE2 after MODULE1
    MODULE2.run_game(name)

if __name__ == "__main__":
    main()

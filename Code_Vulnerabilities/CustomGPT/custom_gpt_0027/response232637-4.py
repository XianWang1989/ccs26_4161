
from package import MODULE1, MODULE2, MODULE3

def main():
    user_input = input('Please enter your question: ').lower().split()

    # Try each module in order
    for module in (MODULE1, MODULE2, MODULE3):
        module.run_game(user_input)

if __name__ == "__main__":
    main()

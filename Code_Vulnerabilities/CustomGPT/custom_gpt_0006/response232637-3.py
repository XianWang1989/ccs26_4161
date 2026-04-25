
from package import *  # Ensure __all__ is set appropriately in your package

def main():
    name = input('Please enter your question: ').lower()

    if len(name) >= 3:
        MODULE1.game_logic(name)
        MODULE2.game_logic(name)
        MODULE3.game_logic(name)
        MODULE4.game_logic(name)

if __name__ == '__main__':
    main()


from package.MODULE1 import game_logic as game_logic1
from package.MODULE2 import game_logic as game_logic2
# Import additional modules as needed...

def main():
    name = input('Please Enter your question: ').lower()

    # Check MODULE1 first
    game_logic1(name)

    # If MODULE1 does not handle the question, check MODULE2
    # You may want to include a way to identify if it was handled in MODULE1
    if name not in ['what is my color', 'color']:  # condition based on MODULE1 logic
        game_logic2(name)

    # Continue with additional modules as necessary, e.g., MODULE3, MODULE4...

if __name__ == "__main__":
    main()


# main_program.py

from package import MODULE1, MODULE2, MODULE3  # Import your modules here

def main():
    question = input('Please Enter your question: ').lower()

    # Define your game logic flow
    if len(question) >= 3:
        if MODULE1.run_game():  # Check if MODULE1's game was successful
            return
        elif MODULE2.run_game():  # which could also return if it was successful
            return
        elif MODULE3.run_game():
            return
        # Add further module calls as necessary

if __name__ == "__main__":
    main()

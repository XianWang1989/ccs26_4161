
from package import MODULE1, MODULE2, MODULE3, MODULE4  # Import specific modules

def main():
    question = input("Please Enter your question: ").lower()

    # Check each module in order
    if any(word in question for word in ['color']):
        MODULE1.play_color_game()
    elif any(word in question for word in ['car']):
        MODULE2.play_car_game()
    # Add further checks for MODULE3, MODULE4, etc.

if __name__ == "__main__":
    main()

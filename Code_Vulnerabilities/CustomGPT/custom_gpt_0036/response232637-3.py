
# main.py
from package import MODULE1, MODULE2

def main():
    question = input('Please enter your question: ').lower()

    if MODULE1.play_color_game():
        return  # Exit if the color game was played
    if MODULE2.play_car_game():
        return  # Exit if the car game was played

    print("No matching game found for your question.")

if __name__ == "__main__":
    main()


from package import MODULE1, MODULE2, MODULE3, MODULE4

def main():
    question = input('Please Enter your question: ').lower()

    result = MODULE1.play_color_game(question)
    if not result:
        result = MODULE2.play_car_game(question)  # Similarly define for MODULE2
    if not result:
        result = MODULE3.play_food_game(question)  # Define in MODULE3
    if not result:
        result = MODULE4.play_toy_game(question)  # Define in MODULE4

    if result:
        print(result)
    else:
        print('No matching game found.')

if __name__ == '__main__':
    main()

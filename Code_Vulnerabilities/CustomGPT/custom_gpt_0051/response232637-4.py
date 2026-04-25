
from package.MODULE1 import game_color
from package.MODULE2 import game_cars
from package.MODULE3 import game_foods

def main():
    question = input('Please Enter your question: ').lower()

    if 'color' in question:
        game_color()
    elif 'car' in question:
        game_cars()
    elif 'food' in question:
        game_foods()
    else:
        print('Sorry, I cannot help with that.')

if __name__ == "__main__":
    main()

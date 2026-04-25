
from package.MODULE1 import check_color
from package.MODULE2 import check_cars
from package.MODULE3 import check_foods

def main():
    name = input('Please Enter your question: ').lower()

    result = check_color(name)
    if result:
        print('You found a color-related question!')
    else:
        result = check_cars(name)
        if result:
            print('You found a car-related question!')
        else:
            result = check_foods(name)
            if result:
                print('You found a food-related question!')
            else:
                print('No matches found!')

if __name__ == "__main__":
    main()

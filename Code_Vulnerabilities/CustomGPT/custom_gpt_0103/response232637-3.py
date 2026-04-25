
from package import module1, module2

def main():
    name = input('Please Enter your question: ').lower()

    # Calling functions from the imported modules
    if 'color' in name:
        module1.play_color_game()
    elif 'vehicle' in name:
        module2.play_vehicle_game()
    else:
        print('No module found for your question.')

if __name__ == "__main__":
    main()

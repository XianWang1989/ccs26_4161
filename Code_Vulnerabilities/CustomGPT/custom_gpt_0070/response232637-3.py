
from package import MODULE1, MODULE2, MODULE3, MODULE4

def main():
    name = input('Please Enter your question: ').lower()

    if len(name) >= 3:
        MODULE1.play_color_game(name)
    if len(name) >= 3:
        MODULE2.play_car_game(name)
    # Call other modules similarly...

if __name__ == "__main__":
    main()

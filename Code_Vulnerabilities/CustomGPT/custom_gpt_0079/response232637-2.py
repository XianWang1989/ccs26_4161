
# MODULE1.py

def process(name2):
    colorLists = ['what is my color', 'color', ... ]

    for item in name2:
        if item in colorLists:
            print('You found the color here')
            name3 = input('What is your favorite color? ')
            respond_to_color(name3)
            return True  # Indicate that this module handled the input
    return False  # Indicate no handling was done

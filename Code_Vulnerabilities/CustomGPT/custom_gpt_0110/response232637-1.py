
def play_game():
    question = input("Please enter your question: ").lower()
    color_lists = ['what is my color', 'color']
    if question in color_lists:
        name3 = input('What is your favorite color? ')
        # Further color processing...
        print('You found the color!')


# MODULE1.py

def run_game():
    name = input('Please Enter your question: ').lower()
    colorLists = ['what is my color', 'color']
    if name in colorLists:
        name3 = input('What is your favorite color? ').lower()
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady.')
        elif name3 == 'blue':
            print('Boys love this.')
        # Add more colors as needed

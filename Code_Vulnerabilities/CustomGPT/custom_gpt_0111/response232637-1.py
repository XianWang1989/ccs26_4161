
# MODULE1.py
def main():
    name = input('Please enter your question: ').lower()
    color_lists = ['red', 'pink', 'blue']
    if any(color in name for color in color_lists):
        print('You found a color here!')
        name3 = input('What is your favorite color? ').lower()
        responses = {
            'red': 'You are hot!',
            'pink': 'You must be a lady',
            'blue': 'Boys love this'
        }
        print(responses.get(name3, 'I do not recognize that color.'))

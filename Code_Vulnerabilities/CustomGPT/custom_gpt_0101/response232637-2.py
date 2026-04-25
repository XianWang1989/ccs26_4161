
# MODULE1.py
def process(question):
    color_lists = ['what is my color', 'color']
    if question in color_lists:
        print('You found the color here')
        name3 = input('What is your favorite color? ').lower()
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady')
        elif name3 == 'blue':
            print('Boys love this')
        return True
    return False

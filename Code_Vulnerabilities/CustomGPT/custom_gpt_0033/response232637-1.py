
def run_module():
    name = input('Please enter your question: ').lower()
    color_lists = ['red', 'pink', 'blue']  # Example list
    if any(color in name for color in color_lists):
        print('You found a color!')

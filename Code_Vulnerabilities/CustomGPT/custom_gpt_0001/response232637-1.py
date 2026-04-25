
def run_module():
    color_lists = ['red', 'pink', 'blue']  # example list; should contain relevant checks.
    name = input('Please Enter your question: ').lower()
    if any(color in name for color in color_lists):
        print('You found the color here!')

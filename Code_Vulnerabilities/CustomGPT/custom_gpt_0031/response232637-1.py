
def run_module():
    name = input('Please enter your question: ').lower()
    color_list = ['red', 'blue', 'pink']
    if any(color in name for color in color_list):
        print('You found a color here!')
    return False  # Indicate if the question is not found

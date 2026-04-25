
def run_module():
    name = input('Please Enter your question: ').lower()
    color_list = ['red', 'pink', 'blue']
    if any(color in name for color in color_list):
        print('You found the color here.')
        name3 = input('What is your favorite color? ').lower()
        if name3 == 'red':
            print('You are hot!')
        elif name3 == 'pink':
            print('You must be a lady!')
        elif name3 == 'blue':
            print('Boys love this!')

# Ensure the function runs only when this module is executed directly, not when imported
if __name__ == "__main__":
    run_module()


def handle_query(query):
    color_lists = ['what is my color', 'color']
    if query in color_lists:
        print('You found the color here!')
        return True
    return False

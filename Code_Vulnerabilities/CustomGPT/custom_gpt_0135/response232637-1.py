
def check_color(input_text):
    color_list = ['red', 'pink', 'blue']
    for color in color_list:
        if color in input_text:
            return f"You found the color: {color}"
    return None


def create_ord_mapping():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    return {char: index for index, char in enumerate(alphabet)}

ord_mapping = create_ord_mapping()

def custom_ord(char):
    return ord_mapping.get(char, -1)  # Return -1 for characters not found

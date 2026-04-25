
def custom_ord(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!"
    for index, value in enumerate(alphabet):
        if value == char:
            return index
    return -1  # Return -1 for characters not in the alphabet

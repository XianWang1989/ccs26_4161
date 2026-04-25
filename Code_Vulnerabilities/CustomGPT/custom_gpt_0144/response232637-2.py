def can_handle(text):
    keywords = ['color', 'what is my color']
    return any(word in text for word in keywords)

def run(text):
    print("You found the color module!")
    color = input("What is your favorite color? ").lower()
    if color == "red":
        print("You are hot!")
    elif color == "pink":
        print("You must be a lady.")
    elif color == "blue":
        print("Boys love this.")
    else:
        print("Nice choice!")

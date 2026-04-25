
# main.py
from package import MODULE1, MODULE2, MODULE3, MODULE4

def run_game(name):
    if MODULE1.game(name):  # Assuming MODULE1.game returns True if it found a match
        return True
    elif MODULE2.game(name):
        return True
    elif MODULE3.game(name):
        return True
    elif MODULE4.game(name):
        return True
    return False

if __name__ == '__main__':
    name = input('Please Enter your question: ').lower()
    run_game(name)

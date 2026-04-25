
# MODULE2.py
def play_game(question):
    carLists = ['car', 'truck', 'bicycle']
    if question in carLists:
        return f"You found a vehicle: {question}!"
    return None

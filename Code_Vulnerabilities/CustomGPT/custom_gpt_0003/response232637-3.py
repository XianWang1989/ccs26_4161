
# Similar structure but for toys
toyLists = ['what is my toy', 'toy', 'ball', 'doll']

def check_toys(input_question):
    if any(toy in input_question for toy in toyLists):
        print("You found a toy!")

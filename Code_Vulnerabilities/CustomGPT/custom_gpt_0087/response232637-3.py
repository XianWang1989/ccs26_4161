
from package.MODULE1 import play_game as play_game1
from package.MODULE2 import play_game as play_game2

name = input('Please Enter your question: ').lower()

# Check MODULE1 first
play_game1(name)

# If not found in MODULE1, check MODULE2
play_game2(name)

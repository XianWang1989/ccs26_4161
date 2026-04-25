
# Prompt user for input
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Find the highest score
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Print the highest score
print("The highest score entered is:", highest_score)

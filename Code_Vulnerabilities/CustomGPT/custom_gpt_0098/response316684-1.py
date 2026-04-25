
# Get user input for three scores
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Find the highest number
highestScore = max(numOneInt, numTwoInt, numThreeInt)

# Store the highest score for further use
print(f"The highest score is: {highestScore}")

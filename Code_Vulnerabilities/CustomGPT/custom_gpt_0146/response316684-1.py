
# Getting user input for the scores
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Storing the highest score
highestScore = max(numOneInt, numTwoInt, numThreeInt)

# Printing the highest score
print(f"The highest score entered is: {highestScore}")

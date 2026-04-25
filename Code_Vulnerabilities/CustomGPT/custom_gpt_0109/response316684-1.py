
# User input
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Store the highest number
highestScore = max(numOneInt, numTwoInt, numThreeInt)

# Output the highest score
print("The highest score is:", highestScore)

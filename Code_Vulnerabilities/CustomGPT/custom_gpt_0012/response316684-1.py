
# Getting user inputs
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Finding the highest number
highestScore = max(numOneInt, numTwoInt, numThreeInt)

# Now, highestScore holds the highest number
print("The highest score is:", highestScore)

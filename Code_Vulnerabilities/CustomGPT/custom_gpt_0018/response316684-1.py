
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Find the highest number
maxScore = max(numOneInt, numTwoInt, numThreeInt)

# Now maxScore holds the highest number
print("The highest score is:", maxScore)

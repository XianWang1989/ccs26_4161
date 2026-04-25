
# Accepting input from the user
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Using the max() function to find the highest score
highestScore = max(numOneInt, numTwoInt, numThreeInt)

# Printing the highest score
print("The highest score is:", highestScore)

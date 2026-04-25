
# Taking inputs from the user
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Finding the highest number
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Storing the highest score for further use
print("The highest score is:", highest_score)

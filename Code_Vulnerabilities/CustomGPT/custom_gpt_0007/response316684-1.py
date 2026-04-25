
# Getting user inputs
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Storing the highest number using the max function
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Printing the highest score for confirmation
print("The highest score is:", highest_score)

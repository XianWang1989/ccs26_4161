
# Input numbers from the user
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Find the maximum value
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Store the highest number for future use
print("The highest score is:", highest_score)

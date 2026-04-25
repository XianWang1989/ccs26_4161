
# Input from the user
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Storing the highest number
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Output the highest number
print("The highest score is:", highest_score)

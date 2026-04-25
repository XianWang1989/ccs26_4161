
# Input for the first number
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

# Input for the second number
numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

# Input for the third number
numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Store the highest number using the max function
highestScore = max(numOneInt, numTwoInt, numThreeInt)

# Print the highest score
print("The highest score is:", highestScore)


# Ask the user for three numbers
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Use the max function to find the highest number
highestScore = max(numOneInt, numTwoInt, numThreeInt)

# Print the highest score
print("The highest score is:", highestScore)

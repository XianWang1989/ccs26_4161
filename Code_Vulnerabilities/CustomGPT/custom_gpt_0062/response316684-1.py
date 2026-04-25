
# Prompt the user for three numbers
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Use max() to find the highest score
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Store the highest number in a variable for future use
print(f"The highest score is: {highest_score}")


# Getting user input for three scores
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Finding the highest number
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Displaying the highest score
print(f"The highest score is: {highest_score}")

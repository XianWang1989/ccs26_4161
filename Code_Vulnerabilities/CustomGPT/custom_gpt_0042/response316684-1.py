
# Asking for user input
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Finding the highest score
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Storing the highest score for future use
print(f"The highest score is: {highest_score}")

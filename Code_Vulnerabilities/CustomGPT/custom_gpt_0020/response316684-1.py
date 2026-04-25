
# Asking the user for three scores
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Storing the highest score
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# You can now use highest_score later in your program
print("The highest score is:", highest_score)

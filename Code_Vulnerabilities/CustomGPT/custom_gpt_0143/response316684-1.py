
# Input for the three scores
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Finding and storing the highest score
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Output the highest score
print("The highest score is:", highest_score)

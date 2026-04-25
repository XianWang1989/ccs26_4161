
# Input numbers from the user
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Find the highest number and store it
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Output the highest score
print("The highest score you entered is:", highest_score)

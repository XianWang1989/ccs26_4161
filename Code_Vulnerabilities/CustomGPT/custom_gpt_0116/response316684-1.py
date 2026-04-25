
# Input scores from the user
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Find the highest score
highestScore = max(numOneInt, numTwoInt, numThreeInt)

# Print the highest score
print(f"The highest score is {highestScore}.")


# Input scores from the user
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Find the highest score
highestScore = max(numOneInt, numTwoInt, numThreeInt)

# Now you can use 'highestScore' for further calculations or in your while loop
print(f"The highest score entered is: {highestScore}")

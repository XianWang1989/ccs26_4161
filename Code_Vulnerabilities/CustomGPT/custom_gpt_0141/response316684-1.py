
# Input scores from the user
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Find the highest number using the max function
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Print the highest score
print("The highest score is:", highest_score)

# You can use `highest_score` for further calculations or logic

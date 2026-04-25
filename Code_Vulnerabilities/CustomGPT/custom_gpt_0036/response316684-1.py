
# Taking user inputs for three scores
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Using the max function to find the highest score
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Storing the highest score for further use
print(f"The highest score entered is: {highest_score}")

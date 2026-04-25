
# Input the three scores
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Use the max() function to find the highest score
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Print the highest score for further use
print(f"The highest score is: {highest_score}")

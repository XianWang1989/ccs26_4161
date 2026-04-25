
# Prompt user for three scores
numOne = int(input("Please enter the first score: "))
numTwo = int(input("Please enter the second score: "))
numThree = int(input("Please enter the third score: "))

# Store the highest score
highest_score = max(numOne, numTwo, numThree)

# Output the highest score
print("The highest score is:", highest_score)

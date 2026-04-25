
# Ask the user to enter three numbers
numOne = int(input("Please enter the first score: "))
numTwo = int(input("Please enter the second score: "))
numThree = int(input("Please enter the third score: "))

# Use the max function to find the highest number
highest_score = max(numOne, numTwo, numThree)

# Store the highest score for further use
print(f"The highest score is: {highest_score}")

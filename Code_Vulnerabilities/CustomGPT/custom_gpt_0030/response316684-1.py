
# Prompting user for input
numOne = int(input("Please enter the first score: "))
numTwo = int(input("Please enter the second score: "))
numThree = int(input("Please enter the third score: "))

# Storing the highest number using the max function
highest_score = max(numOne, numTwo, numThree)

# Output the highest score
print(f"The highest score is: {highest_score}")

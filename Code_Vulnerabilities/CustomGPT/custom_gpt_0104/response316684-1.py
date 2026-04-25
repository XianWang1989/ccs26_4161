
# Input numbers from the user
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Find the highest number
highest_score = max(numOneInt, numTwoInt, numThreeInt)

# Display the highest score
print(f"The highest score is: {highest_score}")

# Now you can use 'highest_score' for further processing in your program.

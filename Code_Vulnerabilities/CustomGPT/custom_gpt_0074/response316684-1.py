
# Getting input from the user
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Finding the highest number
highest_num = max(numOneInt, numTwoInt, numThreeInt)

# Storing the highest number for further use
print(f"The highest number entered is: {highest_num}")

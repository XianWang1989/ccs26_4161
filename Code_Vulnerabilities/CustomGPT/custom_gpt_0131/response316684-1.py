
numOne = input("Please enter the first score: ")
numOneInt = int(numOne)

numTwo = input("Please enter the second score: ")
numTwoInt = int(numTwo)

numThree = input("Please enter the third score: ")
numThreeInt = int(numThree)

# Compare the three numbers and store the highest
highest_num = max(numOneInt, numTwoInt, numThreeInt)

# Now you can use highest_num later in your program
print("The highest score is:", highest_num)

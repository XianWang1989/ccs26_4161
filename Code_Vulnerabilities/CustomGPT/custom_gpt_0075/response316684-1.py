
numOne = int(input("Please enter the first score: "))
numTwo = int(input("Please enter the second score: "))
numThree = int(input("Please enter the third score: "))

highest = numOne  # Assume the first is the highest
if numTwo > highest:
    highest = numTwo
if numThree > highest:
    highest = numThree

print("The highest score is:", highest)

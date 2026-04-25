
# Step 1: Get user inputs
numOne = int(input("Please enter the first score: "))
numTwo = int(input("Please enter the second score: "))
numThree = int(input("Please enter the third score: "))

# Step 2: Find the maximum number
max_num = numOne  # Assume first number is the largest initially
if numTwo > max_num:
    max_num = numTwo  # Update if second number is larger
if numThree > max_num:
    max_num = numThree  # Update if third number is larger

# Step 3: Store and print the maximum number
print("The highest score is:", max_num)

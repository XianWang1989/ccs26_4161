
msg = input("Message? ")
length = len(msg)

# Create a list to hold every third letter
third_letters = []

for i in range(0, length, 3):
    third_letters.append(msg[i])  # Add the letter to the list

# Join the list with a space and print the result
output = " ".join(third_letters)
print(output)

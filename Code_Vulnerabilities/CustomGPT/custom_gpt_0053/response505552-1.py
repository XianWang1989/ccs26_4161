
msg = input("Message? ")
length = len(msg)

# Create a list to hold every third letter
third_letters = []

# Loop through the message and collect every third letter
for i in range(0, length, 3):
    third_letters.append(msg[i])

# Join the list with spaces and print the result
output = " ".join(third_letters)
print(output)

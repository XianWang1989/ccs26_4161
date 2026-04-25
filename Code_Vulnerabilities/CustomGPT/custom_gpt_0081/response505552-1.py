
msg = input("Message? ")
output = []  # Create an empty list to store every third letter

# Collect every third letter from the input message
for i in range(0, len(msg), 3):
    output.append(msg[i])  # Append the letter to the list

# Join the list into a single string with spaces in between and print it
print(" ".join(output))

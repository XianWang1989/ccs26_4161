
msg = input("Message? ")
result = []  # Create an empty list to hold the letters

# Iterate through the message, taking every third letter
for i in range(0, len(msg), 3):
    result.append(msg[i])  # Append the letter to the list

# Join the collected letters with a space and print the result
print(" ".join(result))

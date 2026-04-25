
msg = input("Message? ")
length = len(msg)
letters = []  # Create an empty list to collect letters

for i in range(0, length, 3):
    letters.append(msg[i])  # Append every third letter to the list

# Join the letters with a space and print the result
output = " ".join(letters)
print(output)

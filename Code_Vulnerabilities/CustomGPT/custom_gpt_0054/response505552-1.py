
msg = input("Message? ")
length = len(msg)
letters = []  # List to store every third letter

for i in range(0, length, 3):
    letters.append(msg[i])  # Add the letter to the list

# Join the letters with a space and print
result = " ".join(letters)
print(result)

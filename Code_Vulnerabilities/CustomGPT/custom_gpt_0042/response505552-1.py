
msg = input("Message? ")
length = len(msg)

# Create a list to store every third letter
letters = []

for i in range(0, length, 3):
    letters.append(msg[i])

# Join the letters with a space and print the result
output = " ".join(letters)
print(output)

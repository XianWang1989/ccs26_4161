
msg = input("Message? ")
length = len(msg)

# Use a list to store every third letter
letters = []
for i in range(0, length, 3):
    letters.append(msg[i])

# Join the letters with a space and print
print(" ".join(letters))

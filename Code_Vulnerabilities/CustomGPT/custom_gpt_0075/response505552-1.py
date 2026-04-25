
# Read user input
msg = input("Message? ")
length = len(msg)

# Collect every third letter
letters = []
for i in range(0, length, 3):
    letters.append(msg[i])

# Join and print the letters with a space in between
output = " ".join(letters)
print(output)

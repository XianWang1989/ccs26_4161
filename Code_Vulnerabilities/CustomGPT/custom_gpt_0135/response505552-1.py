
msg = input("Message? ")
length = len(msg)

# Collect every third letter in a list
letters = []
for i in range(0, length, 3):
    letters.append(msg[i])

# Join the collected letters with a space and print
output = " ".join(letters)
print(output)

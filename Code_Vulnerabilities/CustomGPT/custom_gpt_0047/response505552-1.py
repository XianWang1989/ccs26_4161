
msg = input("Message? ")
length = len(msg)

# Collect every third character in a list
letters = []
for i in range(0, length, 3):
    letters.append(msg[i])

# Join the letters with a space and print the result
result = " ".join(letters)
print(result)

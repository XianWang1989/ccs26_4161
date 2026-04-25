
msg = input("Message? ")
length = len(msg)
letters = []

for i in range(0, length, 3):
    letters.append(msg[i])

# Join the letters with a space and print the result
result = " ".join(letters)
print(result)

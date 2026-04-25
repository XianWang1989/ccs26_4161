
msg = input("Message? ")
length = len(msg)
letters = []

for i in range(0, length, 3):
    letters.append(msg[i])

# Join the collected letters with spaces and print
output = " ".join(letters)
print(output)

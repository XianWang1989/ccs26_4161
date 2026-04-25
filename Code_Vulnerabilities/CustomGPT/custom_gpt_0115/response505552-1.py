
msg = input("Message? ")
letters = []

for i in range(0, len(msg), 3):
    letters.append(msg[i])

# Join the letters with a space and print
output = " ".join(letters)
print(output)

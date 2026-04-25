
msg = input("Message? ")
length = len(msg)
output = []

for i in range(0, length, 3):
    output.append(msg[i])

# Join the characters with a space and print the result
print(" ".join(output))

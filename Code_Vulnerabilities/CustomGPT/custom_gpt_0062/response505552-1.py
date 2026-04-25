
msg = input("Message? ")
length = len(msg)
output = []

for i in range(0, length, 3):
    output.append(msg[i])

# Join the collected letters with a space and print
print(" ".join(output))

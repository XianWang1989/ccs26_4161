
msg = input("Message? ")
output = []

for i in range(0, len(msg), 3):
    output.append(msg[i])

# Join the collected letters with a space and print the result
print(" ".join(output))

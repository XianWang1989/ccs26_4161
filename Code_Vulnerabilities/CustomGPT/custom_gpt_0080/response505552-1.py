
msg = input("Message? ")
length = len(msg)
result = []

for i in range(0, length, 3):
    result.append(msg[i])

# Join the collected characters with a space and print
output = " ".join(result)
print(output)


msg = input("Message? ")
length = len(msg)
result = []

for i in range(0, length, 3):
    result.append(msg[i])

# Join the characters with a space and print the result
print(" ".join(result))


msg = input("Message? ")
length = len(msg)

# Collect every third character
result = []
for i in range(0, length, 3):
    result.append(msg[i])

# Join with a space and print
output = " ".join(result)
print(output)

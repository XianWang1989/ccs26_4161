
msg = input("Message? ")
result = []

length = len(msg)
for i in range(0, length, 3):
    result.append(msg[i])

# Join the collected characters with a space
output = " ".join(result)
print(output)

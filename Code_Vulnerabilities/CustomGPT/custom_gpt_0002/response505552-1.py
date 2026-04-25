
msg = input("Message? ")
length = len(msg)
result = []

for i in range(0, length, 3):
    result.append(msg[i])

output = " ".join(result)
print(output)

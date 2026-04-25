
msg = input("Message? ")
length = len(msg)
result = []

for i in range(0, length, 3):
    result.append(msg[i])

# Join the results with spaces and print
output = " ".join(result)
print(output)

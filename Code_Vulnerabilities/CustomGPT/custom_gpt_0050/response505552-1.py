
msg = input("Message? ")
length = len(msg)
result = []

for i in range(0, length, 3):
    result.append(msg[i])

# Join the list into a single string with spaces and print it
output = " ".join(result)
print(output)

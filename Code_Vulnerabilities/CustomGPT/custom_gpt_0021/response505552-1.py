
msg = input("Message? ")
length = len(msg)
result = []

for i in range(0, length, 3):
    result.append(msg[i])

# Join the letters with a space and print them
output = " ".join(result)
print(output)

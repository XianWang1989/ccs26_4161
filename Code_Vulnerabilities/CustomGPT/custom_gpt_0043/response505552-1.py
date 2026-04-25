
msg = input("Message? ")
length = len(msg)
result = []

for i in range(0, length, 3):
    result.append(msg[i])

# Join the collected letters with a space and print the final result
output = " ".join(result)
print(output)

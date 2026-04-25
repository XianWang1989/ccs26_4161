
msg = input("Message? ")
length = len(msg)

# Collect every third letter
result = []
for i in range(0, length, 3):
    result.append(msg[i])

# Join the collected letters with a space
output = ' '.join(result)
print(output)

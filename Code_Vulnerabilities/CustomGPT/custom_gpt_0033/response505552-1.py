
msg = input("Message? ")
length = len(msg)
result = []

# Collect every third letter
for i in range(0, length, 3):
    result.append(msg[i])

# Join the letters with a space and print
output = " ".join(result)
print(output)

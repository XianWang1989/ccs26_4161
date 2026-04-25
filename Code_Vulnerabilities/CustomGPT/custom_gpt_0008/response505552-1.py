
msg = input("Message? ")
result = []

# Iterate over every third letter
for i in range(0, len(msg), 3):
    result.append(msg[i])

# Join the characters with a space and print
output = " ".join(result)
print(output)

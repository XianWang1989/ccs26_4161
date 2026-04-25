
msg = input("Message? ")
result = []

# Read every third letter
for i in range(0, len(msg), 3):
    result.append(msg[i])

# Join the collected letters with spaces
output = " ".join(result)
print(output)

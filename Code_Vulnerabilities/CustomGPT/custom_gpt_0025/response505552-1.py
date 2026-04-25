
msg = input("Message? ")
length = len(msg)

# Collect every third letter
output = []
for i in range(0, length, 3):
    output.append(msg[i])

# Join the list into a single string with spaces in between
result = " ".join(output)
print(result)

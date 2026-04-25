
msg = input("Message? ")
result = []

# Collect every third letter
for i in range(0, len(msg), 3):
    result.append(msg[i])

# Join the collected letters with a space and print
output = " ".join(result)
print(output)

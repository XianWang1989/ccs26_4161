
msg = input("Message? ")
output = []

# Collect every third letter
for i in range(0, len(msg), 3):
    output.append(msg[i])

# Join the characters with a space and print
print(" ".join(output))

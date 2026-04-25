
msg = input("Message? ")
length = len(msg)
output = []

# Collect every third letter
for i in range(0, length, 3):
    output.append(msg[i])

# Join the letters with a space and print
print(" ".join(output))

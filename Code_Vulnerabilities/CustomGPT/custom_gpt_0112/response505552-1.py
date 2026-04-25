
msg = input("Message? ")
output = []

# Read every third letter
for i in range(0, len(msg), 3):
    output.append(msg[i])

# Join the collected letters with a space and print
print(" ".join(output))

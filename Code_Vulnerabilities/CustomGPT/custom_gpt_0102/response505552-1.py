
msg = input("Message? ")
result = []

# Read every third letter
for i in range(0, len(msg), 3):
    result.append(msg[i])

# Join the letters with a space and print
print(" ".join(result))

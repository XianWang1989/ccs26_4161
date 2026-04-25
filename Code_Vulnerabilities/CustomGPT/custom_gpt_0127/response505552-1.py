
msg = input("Message? ")
length = len(msg)

# Collect every third letter in a list
result = []
for i in range(0, length, 3):
    result.append(msg[i])

# Join the letters with a space and print them
print(" ".join(result))


msg = input("Message? ")
result = []

for i in range(0, len(msg), 3):
    result.append(msg[i])

# Join the list with spaces and print
print(" ".join(result))

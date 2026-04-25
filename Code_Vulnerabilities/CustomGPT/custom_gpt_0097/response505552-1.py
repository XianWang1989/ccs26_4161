
msg = input("Message? ")
output = []

for i in range(0, len(msg), 3):
    output.append(msg[i])

print(" ".join(output))

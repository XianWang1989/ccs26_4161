
msg = input("Message? ")
output = []  # List to store every third letter

for i in range(0, len(msg), 3):
    output.append(msg[i])  # Append every third letter to the list

# Join the list with a space and print it
print(" ".join(output))

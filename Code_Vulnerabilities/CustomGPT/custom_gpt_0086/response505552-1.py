
msg = input("Message? ")
result = []

# Read every third letter and append to the result list
for i in range(0, len(msg), 3):
    result.append(msg[i])

# Join the list into a string with spaces and print it
print(" ".join(result))

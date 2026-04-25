
msg = input("Message? ")
length = len(msg)

# Collect every third letter in a list
letters = [msg[i] for i in range(0, length, 3)]

# Join the letters with a space and print the result
result = " ".join(letters)
print(result)

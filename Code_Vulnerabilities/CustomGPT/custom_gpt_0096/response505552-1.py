
msg = input("Message? ")
length = len(msg)

# Create a list of every third letter
third_letters = [msg[i] for i in range(0, length, 3)]

# Join the letters with a space and print them
output = " ".join(third_letters)
print(output)

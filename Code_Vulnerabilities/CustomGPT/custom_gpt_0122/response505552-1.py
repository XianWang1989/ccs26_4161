
msg = input("Message? ")
# Create a list of every third character
third_chars = [msg[i] for i in range(0, len(msg), 3)]
# Join the characters with a space and print
output = " ".join(third_chars)
print(output)


msg = input("Message? ")
# Create a list of every third letter
letters = [msg[i] for i in range(0, len(msg), 3)]
# Join the letters with a space and print
output = " ".join(letters)
print(output)

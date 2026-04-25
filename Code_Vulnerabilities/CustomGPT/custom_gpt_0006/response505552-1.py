
msg = input("Message? ")
# Create a list of every third letter
third_letters = [msg[i] for i in range(0, len(msg), 3)]
# Join the letters with a space
output = " ".join(third_letters)
print(output)

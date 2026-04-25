
msg = input("Message? ")
length = len(msg)

# Create a list to hold every third letter
third_letters = []

for i in range(0, length, 3):
    third_letters.append(msg[i])

# Join the letters with a space and print
output = " ".join(third_letters)
print(output)

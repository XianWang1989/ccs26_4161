
msg = input("Message? ")
length = len(msg)
letters = []  # Create a list to collect the letters

for i in range(0, length, 3):
    x = msg[i]
    letters.append(x)  # Add the letter to the list

# Join the letters with a space and print them all at once
output = " ".join(letters)
print(output)

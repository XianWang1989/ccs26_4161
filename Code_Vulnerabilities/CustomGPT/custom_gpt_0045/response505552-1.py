
msg = input("Message? ")
length = len(msg)
# Create a list to hold the selected letters
letters = []

for i in range(0, length, 3):
    letters.append(msg[i])  # Add the selected letter to the list

# Join the letters with a space and print them
print(" ".join(letters))


# Get input from the user
msg = input("Message? ")

# Initialize a list to hold the selected letters
selected_letters = []

# Loop through the message, picking every third letter
for i in range(0, len(msg), 3):
    selected_letters.append(msg[i])  # Add the letter to the list

# Join the letters with a space and print the result
result = ' '.join(selected_letters)
print(result)

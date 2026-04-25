
msg = input("Message? ")
result = []  # Step 2: Initialize an empty list

# Step 3: Loop through the message with a step of 3
for i in range(0, len(msg), 3):
    result.append(msg[i])  # Step 4: Append the character to the list

# Step 5: Join the list into a string with spaces and print it
print(" ".join(result))

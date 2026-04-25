
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the result
    s = ''

    # Iterate over each line in the file
    for line in fh:
        # Strip the newline characters from the line and add to the string
        s += line.strip()  # .strip() removes any leading/trailing whitespace including newlines

# Print the final result
print(s)

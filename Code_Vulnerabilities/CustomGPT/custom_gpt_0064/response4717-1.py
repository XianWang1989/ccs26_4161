
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the content
    s = ''

    # Iterate over each line in the file
    for line in fh:
        # Remove newline characters and add the line to the string
        s += line.strip()

# Print the final string without any newlines
print(s)


# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the processed content
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and add to the string
        s += line.strip()

# Print the resulting string without any newlines
print(s)


# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the result
    s = ''

    # Loop through the file line by line
    for line in fh:
        # Remove newline characters and concatenate to 's'
        s += line.strip()

# Print the resulting string without any newlines
print(s)

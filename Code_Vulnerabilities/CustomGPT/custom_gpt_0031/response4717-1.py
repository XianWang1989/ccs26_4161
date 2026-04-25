
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the content
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and concatenate to the string
        s += line.strip()

# Print the final string
print(s)

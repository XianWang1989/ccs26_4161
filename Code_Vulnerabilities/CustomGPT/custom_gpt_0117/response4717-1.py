
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for the result
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and add the line to the string
        s += line.strip()

# Print the final string
print(s)

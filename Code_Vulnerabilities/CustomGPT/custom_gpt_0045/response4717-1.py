
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to collect all the lines
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove any newline characters and append to the string
        s += line.strip()

# Print the resulting string
print(s)

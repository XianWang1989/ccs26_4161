
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for concatenation
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and concatenate
        s += line.strip()

# Print the resulting string
print(s)

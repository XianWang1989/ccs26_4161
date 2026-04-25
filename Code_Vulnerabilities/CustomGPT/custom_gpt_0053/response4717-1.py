
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the processed content
    s = ''
    # Read the file line by line
    for line in fh:
        # Remove newline characters and append to the string
        s += line.rstrip('\n')

# Print the processed string
print(s)

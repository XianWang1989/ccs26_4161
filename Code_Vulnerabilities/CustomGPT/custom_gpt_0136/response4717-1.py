
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the processed content
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and append to string
        s += line.strip()  # Using strip to remove '\n'

# Print the final processed string
print(s)

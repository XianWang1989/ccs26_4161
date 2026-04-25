
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to accumulate the content
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove new line characters and accumulate the content
        s += line.strip()  # Using strip() to remove whitespace and new line characters

# Print the concatenated string
print(s)

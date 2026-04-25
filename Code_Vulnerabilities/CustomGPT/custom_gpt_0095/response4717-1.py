
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store content
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove any newline characters and append to s
        s += line.strip()

# Print the final string without any newlines
print(s)

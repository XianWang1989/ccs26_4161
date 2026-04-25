
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the result
    s = ''
    # Read the file line by line
    for line in fh:
        # Remove newline characters and add to the string
        s += line.strip()

# Print the resulting string
print(s)

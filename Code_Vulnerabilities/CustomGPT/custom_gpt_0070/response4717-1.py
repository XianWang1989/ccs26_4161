
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the contents
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and accumulate the string
        s += line.strip()

# Print the final result
print(s)

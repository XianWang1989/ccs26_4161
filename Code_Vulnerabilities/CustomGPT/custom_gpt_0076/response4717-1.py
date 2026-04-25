
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the results
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and add to the string
        s += line.strip()

# Print the processed string
print(s)

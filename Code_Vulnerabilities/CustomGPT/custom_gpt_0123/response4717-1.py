
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store results
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove new line characters and update the string
        s += line.strip()

# Print the final result
print(s)

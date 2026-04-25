
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the result
    s = ''
    # Read the file line by line
    for line in fh:
        # Append the line to the string, removing newlines
        s += line.rstrip('\n')

# Print the resulting string without newlines
print(s)

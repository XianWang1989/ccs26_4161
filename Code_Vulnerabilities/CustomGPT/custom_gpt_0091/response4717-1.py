
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to accumulate the content
    s = ''

    # Read the file line by line
    for line in fh:
        # Strip the newline character and concatenate
        s += line.strip()

# Print the final string
print(s)

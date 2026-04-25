
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Process the file line by line
    s = ''
    for line in fh:
        # Remove newline characters
        s += line.strip()

# Print the final string
print(s)


# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for the combined content
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters from each line and append to the string
        s += line.strip()

# Print the combined result
print(s)

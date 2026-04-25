
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the processed lines
    s = ''

    # Iterate over each line in the file
    for line in fh:
        # Remove newline characters and accumulate the result
        s += line.strip()

# Print the resulting string
print(s)

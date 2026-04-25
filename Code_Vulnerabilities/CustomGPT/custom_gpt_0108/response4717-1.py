
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the processed lines
    s = ''

    # Read the file line by line
    for line in fh:
        # Replace newline characters and concatenate
        s += line.strip()  # Use strip to remove any leading/trailing whitespace

# Print the final string
print(s)

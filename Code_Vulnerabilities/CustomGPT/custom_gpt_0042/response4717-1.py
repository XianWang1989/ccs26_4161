
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the concatenated data
    s = ''

    # Read and process the file line by line
    for line in fh:
        # Remove newline characters and add to the string
        s += line.strip()

# Print the final combined string
print(s)

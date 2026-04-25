
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to accumulate the processed lines
    s = ''

    # Iterate over each line in the file
    for line in fh:
        # Remove any newline characters and add to s
        s += line.strip()

# Print the final result
print(s)

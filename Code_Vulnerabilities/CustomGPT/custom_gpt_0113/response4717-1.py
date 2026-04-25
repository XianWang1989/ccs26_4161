
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to accumulate results
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and accumulate the result
        s += line.strip()  # strip() removes leading/trailing whitespace

# Print the processed string
print(s)

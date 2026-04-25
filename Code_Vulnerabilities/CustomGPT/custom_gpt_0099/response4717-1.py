
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the result
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and add to s
        s += line.strip()  # strip() removes leading and trailing whitespace

# Print the final result
print(s)

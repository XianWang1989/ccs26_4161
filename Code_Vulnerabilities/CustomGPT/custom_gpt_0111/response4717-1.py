
# Open the file using a context manager
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for storing results
    s = ''

    # Process the file line by line
    for line in fh:
        # Remove newline characters and concatenate
        s += line.strip()  # strip() removes leading/trailing whitespace including newlines

# Print the final result
print(s)

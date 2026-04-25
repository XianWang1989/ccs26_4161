
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the result
    s = ''

    # Read and process the file line by line
    for line in fh:
        # Remove newline characters and add to the result
        s += line.strip()  # Use strip to eliminate any leading/trailing whitespace including newlines

# Output the final result
print(s)

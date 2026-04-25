
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to accumulate results
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and accumulate results
        s += line.strip()  # Use strip to remove leading/trailing spaces/newlines

# Print the processed content
print(s)

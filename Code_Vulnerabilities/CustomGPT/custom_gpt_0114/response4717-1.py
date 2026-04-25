
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the content
    s = ''
    # Read the file line by line
    for line in fh:
        # Process each line as needed
        s += line.strip()  # Remove any leading/trailing whitespace

# Print the result
print(s)

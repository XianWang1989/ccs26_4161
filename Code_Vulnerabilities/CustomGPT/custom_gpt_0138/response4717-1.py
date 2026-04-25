
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize a variable to store the processed content
    s = ''
    # Read the file line by line
    for line in fh:
        # Remove newlines and append to 's'
        s += line.strip()  # strip() removes leading/trailing whitespace

# Print the processed content
print(s)

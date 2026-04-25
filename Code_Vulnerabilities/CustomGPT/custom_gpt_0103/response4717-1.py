
# Open the file using 'with' to ensure it's properly closed afterward
with open('reg.fa', 'r') as fh:
    # Initialize an empty string for the result
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and add the line to the string
        s += line.strip()  # strip() removes leading/trailing whitespace and newlines

# Print the final result
print(s)

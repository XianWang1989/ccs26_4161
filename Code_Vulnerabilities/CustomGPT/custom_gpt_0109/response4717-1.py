
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to gather the results
    s = ''

    # Read the file line by line
    for line in fh:
        # Optionally, process the line (remove newlines)
        s += line.strip()  # Strip removes leading/trailing whitespace and newlines

# Output the final string
print(s)


# Using a context manager to open the file safely
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store processed lines
    s = ''

    # Loop through each line in the file
    for line in fh:
        # Strip newline characters from the line and append it to s
        s += line.strip()  # This removes the newline and any leading/trailing whitespace

# Print the result
print(s)


# Open the file using a context manager to ensure it's properly closed
with open('reg.fa', 'r') as fh:
    s = '' 
    # Read the file line by line
    for line in fh:
        # Remove newline characters and concatenate to the `s` variable
        s += line.strip()  # Using strip() to remove whitespace including newlines

# Now `s` contains the content of the file without newlines
print(s)

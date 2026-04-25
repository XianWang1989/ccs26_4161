
# Open the file using a context manager
with open('reg.fa', 'r') as fh:
    s = ''

    # Read line by line
    for line in fh:
        s += line.strip()  # Remove newline and whitespace

print(s)


# Open the file using a context manager to ensure proper closure
with open('reg.fa', 'r') as fh:
    s = ''
    # Iterate over each line in the file
    for line in fh:
        # Remove newline characters from each line
        s += line.strip()

print(s)

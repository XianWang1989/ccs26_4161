
# Improved file handling for large files
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        # Process each line as needed; here, we're concatenating
        s += line.strip()  # Use strip to remove newline characters

print(s)

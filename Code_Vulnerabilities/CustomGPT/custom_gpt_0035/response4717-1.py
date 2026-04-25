
# Efficient file handling for large files
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:  # Read the file line by line
        s += line.strip()  # Remove newline characters and accumulate the string

print(s)

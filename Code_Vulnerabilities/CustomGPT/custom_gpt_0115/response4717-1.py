
# Example of reading a large file line by line
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        s += line.strip()  # Remove newlines and accumulate the content

print(s)  # Output the content without newlines

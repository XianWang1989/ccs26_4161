
# Using a context manager to handle the file
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        s += line.strip()  # Strip newline characters and accumulate

print(s)

# Open the file for reading
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        # Strip newline characters and append to s
        s += line.strip()

print(s)

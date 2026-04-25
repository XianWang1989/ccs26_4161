
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        s += line.strip()  # Remove newline characters and concatenate

print(s)

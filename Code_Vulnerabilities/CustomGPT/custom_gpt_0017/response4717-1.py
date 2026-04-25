
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        s += line.strip()  # strip removes any leading/trailing whitespace

print(s)

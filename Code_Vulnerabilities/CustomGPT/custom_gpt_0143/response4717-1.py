
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        s += line.strip()  # Remove any leading/trailing whitespace
    print(s)

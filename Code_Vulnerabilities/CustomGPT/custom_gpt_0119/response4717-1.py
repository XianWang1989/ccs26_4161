
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        s += line.strip()  # Removing newlines and adding to string

print(s)

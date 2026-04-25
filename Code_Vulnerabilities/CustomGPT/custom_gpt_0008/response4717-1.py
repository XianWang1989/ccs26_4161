
# Open the file and process it line by line
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        s += line.strip()  # Strip newline characters

print(s)

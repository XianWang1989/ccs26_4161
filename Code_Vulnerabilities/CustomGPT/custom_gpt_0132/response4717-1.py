
# Open the file and process it line by line
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        s += line.strip()  # Remove newline characters and accumulate the string

# Now `s` contains the processed string without newlines
print(s)

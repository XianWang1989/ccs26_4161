
# Open the file and process line by line
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        s += line.strip()  # Remove newlines and accumulate the string

print(s)  # Print the concatenated result


# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to collect lines
    s = ''
    # Read file line by line
    for line in fh:
        # Strip newlines and add to the string
        s += line.strip()  # or use s += line.rstrip() to remove only trailing newlines

# Print the resulting string
print(s)


# Open the file in read mode
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        # Strip the newline character and concatenate
        s += line.strip()

# Print the final result
print(s)

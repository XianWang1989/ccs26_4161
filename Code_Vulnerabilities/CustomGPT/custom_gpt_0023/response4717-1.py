
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    s = ''

    # Read the file line by line
    for line in fh:
        # Use strip to remove newlines and concatenate
        s += line.strip()

# Print the result
print(s)

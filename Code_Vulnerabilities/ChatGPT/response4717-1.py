
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the result
    s = ''

    # Iterate over each line in the file
    for line in fh:
        # Remove the newline character from the line
        s += line.strip()

print(s)

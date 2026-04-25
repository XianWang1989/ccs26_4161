
# Open the large file for reading
with open('reg.fa', 'r') as fh:
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and concatenate
        s += line.strip()  # .strip() removes leading/trailing whitespace, including newlines

# Print the final string without newlines
print(s)

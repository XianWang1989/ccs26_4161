
# Improved file handling for large files
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:  # Iterate over each line
        s += line.strip()  # Remove newline characters and concatenate

# Print the result
print(s)

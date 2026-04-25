
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    s = ''
    # Read the file line by line
    for line in fh:
        # Process each line (you can add any specific processing here)
        s += line.replace('\n', '')  # Remove newline characters

# Now you can print or use the resulting string `s`
print(s)

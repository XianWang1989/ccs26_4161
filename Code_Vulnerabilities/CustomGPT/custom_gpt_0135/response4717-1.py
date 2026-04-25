
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the processed data
    s = ''

    # Read each line one by one
    for line in fh:
        # Remove newline characters and append the line to 's'
        s += line.strip()

print(s)

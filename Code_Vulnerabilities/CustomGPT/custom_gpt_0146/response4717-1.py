
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to store the contents
    s = ''

    # Iterate over each line in the file
    for line in fh:
        # Remove newline characters
        line = line.strip()  
        # Append the cleaned line to the string
        s += line

# Output the processed content
print(s)

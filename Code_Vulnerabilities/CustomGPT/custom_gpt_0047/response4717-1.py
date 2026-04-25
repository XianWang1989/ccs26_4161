
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the content
    s = ''

    # Read the file line by line
    for line in fh:
        # Remove newline characters and add to the string
        s += line.strip()  # using strip() to remove leading/trailing whitespace

# Now you can do something with the final string 's'
print(s)

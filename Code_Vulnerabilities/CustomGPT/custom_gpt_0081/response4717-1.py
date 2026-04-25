
# Open the file in read mode
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold the processed lines
    s = ''

    # Iterate through each line in the file
    for line in fh:
        # Remove the newline character and append to the string
        s += line.strip()

# At this point, `s` contains the entire content of the file without newlines
print(s)

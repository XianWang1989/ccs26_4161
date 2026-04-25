
# Opening the file
with open('reg.fa', 'r') as fh:
    s = ''
    # Reading the file line by line
    for line in fh:
        # Removing newline characters and concatenate to string
        s += line.strip()  # strip() removes leading/trailing whitespace including '\n'

# At this point, 's' contains the entire content of the file without newline characters
print(s)

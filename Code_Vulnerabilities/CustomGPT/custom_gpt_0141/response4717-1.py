
# Open the file for reading
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to collect the processed lines
    s = ''
    # Loop through each line in the file
    for line in fh:
        # Remove newline characters and append to the string
        s += line.strip()  # Using strip() to remove leading/trailing whitespace, including newline characters

# To check the output after processing
print(s)


# Opening the file in read mode
with open('reg.fa', 'r') as fh:
    # Reading the file line by line to handle large files
    for line in fh:
        # Optional: process the line as needed 
        # For example, strip new line characters
        cleaned_line = line.strip()
        print(cleaned_line)

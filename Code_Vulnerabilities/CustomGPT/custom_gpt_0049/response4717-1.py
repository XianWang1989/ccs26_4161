
with open('reg.fa', 'r') as fh:
    for line in fh:
        # Process each line - for example, removing newline characters
        processed_line = line.strip()
        print(processed_line)  # or perform other processing

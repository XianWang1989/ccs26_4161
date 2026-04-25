
with open('reg.fa', 'r') as fh:
    # Use a generator to process each line
    for line in fh:
        # Process the line (e.g., remove newlines)
        processed_line = line.strip()  # This removes leading and trailing whitespace including newlines
        print(processed_line)  # Or accumulate results as needed

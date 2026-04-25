
# Using a generator to read the file line by line
def process_large_file(filename):
    with open(filename, 'r') as fh:
        for line in fh:
            # Process each line (remove newline characters as needed)
            processed_line = line.strip()  # Removes leading/trailing whitespace
            print(processed_line)  # Replace this with your processing logic

# Call the function with your file
process_large_file('reg.fa')

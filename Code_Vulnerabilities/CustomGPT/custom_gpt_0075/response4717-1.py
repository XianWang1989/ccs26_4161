
# Optimized code to handle large files
def process_large_file(file_path):
    with open(file_path, 'r') as fh:  # Using 'with' ensures files are closed properly
        for line in fh:  # Iterate over file line by line
            line = line.strip()  # Remove any leading/trailing whitespace
            # Process the line as needed, e.g., print it or store it
            print(line)  # Replace this with your logic for processing

# Usage example
process_large_file('reg.fa')

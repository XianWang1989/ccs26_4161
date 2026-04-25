
def process_large_file(file_path):
    with open(file_path, 'r') as fh:
        for line in fh:  # Read each line one at a time
            line = line.strip()  # Remove leading/trailing whitespace
            # Process your line here
            print(line)  # Example action: print the line

# Usage
process_large_file('reg.fa')

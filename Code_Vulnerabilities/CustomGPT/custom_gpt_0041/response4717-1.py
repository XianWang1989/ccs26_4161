
# Define a function to process the file line by line
def process_large_file(filename):
    with open(filename, 'r') as fh:
        for line in fh:
            # Process each line as needed
            processed_line = line.strip()  # Remove newlines and spaces
            # Store or handle the processed line here
            print(processed_line)  # Example action

# Call the function with your file name
process_large_file('reg.fa')

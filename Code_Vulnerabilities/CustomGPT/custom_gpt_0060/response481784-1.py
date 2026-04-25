
import sys
import csv

def construct_line(label, line):
    new_line = []

    # Use '1' instead of '0' for LIBSVM format
    if float(label) == 0.0:
        label = "0"
    else:
        label = "1"

    new_line.append(label)

    for i, item in enumerate(line):
        # Ignore empty features and zeros
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"  # LIBSVM expects 1-based index
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# ---

# Ensure the script receives enough arguments
if len(sys.argv) < 3:
    print("Usage: python csv_to_libsvm.py <input_file> <output_file> [label_index=0] [skip_headers=0]")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Set label index or default to 0
label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0

# Determine whether to skip headers
skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

# Open input and output files
with open(input_file, 'r') as i, open(output_file, 'w') as o:
    reader = csv.reader(i)

    # Skip headers if necessary
    if skip_headers:
        next(reader)

    for line in reader:
        if label_index >= len(line):
            print(f"Warning: Label index {label_index} is out of range for the line: {line}")
            continue

        # Pop the label from the line
        label = line.pop(label_index)

        # Construct the LIBSVM-formatted line
        new_line = construct_line(label, line)

        # Write to output file
        o.write(new_line)

print(f"Converted '{input_file}' to '{output_file}' in LIBSVM format.")

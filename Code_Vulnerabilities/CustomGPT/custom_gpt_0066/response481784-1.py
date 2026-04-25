
import sys
import csv

def construct_line(label, line):
    new_line = [str(label)]  # Start with the label
    for i, item in enumerate(line):
        if item and float(item) != 0.0:  # Check for non-empty and non-zero items
            new_line.append(f"{i + 1}:{item}")
    return " ".join(new_line) + "\n"

# Input and output files
input_file = sys.argv[1]
output_file = sys.argv[2]

# Optional parameters
label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

with open(input_file, 'r', newline='') as i:
    with open(output_file, 'w', newline='') as o:
        reader = csv.reader(i)
        if skip_headers:
            next(reader)  # Skip the header row

        for line in reader:
            if label_index == -1:
                label = '1'  # Default label if none specified
            else:
                label = line.pop(label_index)  # Get the label from the specified index

            new_line = construct_line(label, line)  # Convert to LIBSVM format
            o.write(new_line)  # Write the new line to the output file

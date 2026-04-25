
import sys
import csv

def construct_line(label, line):
    new_line = []
    # Convert label to string if it's not already
    new_line.append(str(label))

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# Read input and output file paths from command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    label_index = int(sys.argv[3])
except IndexError:
    label_index = 0

try:
    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False
except ValueError:
    skip_headers = False

# Open the input and output files
with open(input_file, 'r') as i, open(output_file, 'w') as o:
    reader = csv.reader(i)

    if skip_headers:
        # Skip header line if specified
        next(reader)

    for line in reader:
        if label_index == -1:
            label = '1'  # Default label if none is specified
        else:
            label = line.pop(label_index)  # Extract the label from the line

        new_line = construct_line(label, line)
        o.write(new_line)

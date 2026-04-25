
import sys
import csv

def construct_line(label, line):
    new_line = []
    if float(label) == 0.0:
        label = "0"
    new_line.append(label)

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# File handling and conversion
input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    label_index = int(sys.argv[3])
except IndexError:
    label_index = 0

skip_headers = sys.argv[4].lower() == 'true' if len(sys.argv) > 4 else False

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    reader = csv.reader(infile)

    if skip_headers:
        next(reader)  # Skip header row if specified

    for line in reader:
        # Handle cases where the label index is out of bounds
        if label_index >= len(line):
            continue

        label = line.pop(label_index) if label_index != -1 else '1'
        new_line = construct_line(label, line)
        outfile.write(new_line)

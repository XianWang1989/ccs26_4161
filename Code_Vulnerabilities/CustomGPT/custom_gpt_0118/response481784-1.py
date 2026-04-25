
import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(label)

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# Input and output file names
input_file = sys.argv[1]
output_file = sys.argv[2]

# Label index and skip headers flag
label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    reader = csv.reader(infile)

    if skip_headers:
        next(reader)  # Skip header row if specified

    for line in reader:
        if label_index == -1:
            label = '1'  # If no label, default to '1'
        else:
            label = line.pop(label_index)  # Retrieve and remove label from line

        new_line = construct_line(label, line)
        outfile.write(new_line)

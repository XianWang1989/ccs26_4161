
import sys
import csv

def construct_line(label, line):
    new_line = [label]  # Start with the label
    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:  # Skip empty or zero values
            continue
        new_item = f"{i + 1}:{item}"  # LIBSVM format
        new_line.append(new_item)
    return " ".join(new_line) + "\n"

# Command line arguments handling
input_file = sys.argv[1]
output_file = sys.argv[2]

# Optional arguments for label index and skipping headers
label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

with open(input_file, 'r') as i, open(output_file, 'w') as o:
    reader = csv.reader(i)

    if skip_headers:
        next(reader)  # Skip the header row

    for line in reader:
        label = line.pop(label_index) if label_index != -1 else '1'
        new_line = construct_line(label, line)
        o.write(new_line)

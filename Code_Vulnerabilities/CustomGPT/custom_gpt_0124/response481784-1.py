
import sys
import csv

def construct_line(label, line):
    new_line = [label]  # Start with the label
    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)
    return " ".join(new_line) + "\n"

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    label_index = int(sys.argv[3])
except IndexError:
    label_index = 0

try:
    skip_headers = int(sys.argv[4])
except IndexError:
    skip_headers = 0

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    reader = csv.reader(infile)

    # Skip headers if specified
    if skip_headers:
        next(reader)

    for line in reader:
        label = line.pop(label_index) if label_index != -1 else '1'
        new_line = construct_line(label, line)
        outfile.write(new_line)

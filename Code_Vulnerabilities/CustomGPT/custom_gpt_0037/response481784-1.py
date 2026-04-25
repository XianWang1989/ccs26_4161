
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

# Usage: python csv_to_libsvm.py input.csv output.svm label_index [skip_headers]
input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    label_index = int(sys.argv[3])
except IndexError:
    label_index = 0

try:
    skip_headers = sys.argv[4] == '1'
except IndexError:
    skip_headers = False

with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)

    if skip_headers:
        next(reader)  # Skip header row

    for line in reader:
        if label_index == -1:
            label = '1'  # Default label if label index is -1
        else:
            label = line.pop(label_index)

        new_line = construct_line(label, line)
        outfile.write(new_line)

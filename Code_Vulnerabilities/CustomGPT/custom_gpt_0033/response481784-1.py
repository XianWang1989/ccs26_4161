
import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(str(int(label)))  # Ensure label is an integer string

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# Input: CSV file path, Output: LIBSVM file path, Label index, Skip headers
input_file = sys.argv[1]
output_file = sys.argv[2]

label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
skip_headers = sys.argv[4] if len(sys.argv) > 4 else '0'

with open(input_file, 'r', newline='') as i, open(output_file, 'w', newline='') as o:
    reader = csv.reader(i)
    if skip_headers == '1':
        next(reader)  # Skip header row

    for line in reader:
        if label_index == -1:
            label = '1'
        else:
            label = line.pop(label_index)

        new_line = construct_line(label, line)
        o.write(new_line)

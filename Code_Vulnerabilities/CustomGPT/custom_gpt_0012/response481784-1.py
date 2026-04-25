
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
        new_item = "%s:%s" % (i + 1, item)
        new_line.append(new_item)
    return " ".join(new_line) + "\n"

# ----

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    label_index = int(sys.argv[3])
except IndexError:
    label_index = 0

try:
    skip_headers = int(sys.argv[4]) if len(sys.argv) > 4 else 0
except ValueError:
    skip_headers = 0

with open(input_file, 'r') as i, open(output_file, 'w') as o:
    reader = csv.reader(i)

    if skip_headers:
        next(reader)  # Skip the header if specified

    for line in reader:
        if label_index == -1:
            label = '1'
        else:
            label = line.pop(label_index)

        new_line = construct_line(label, line)
        o.write(new_line)

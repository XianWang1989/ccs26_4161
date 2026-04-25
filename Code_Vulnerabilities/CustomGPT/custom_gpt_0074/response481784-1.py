
import sys
import csv

def construct_line(label, line):
    new_line = []
    # Ensure label is either "0" or "1"
    if float(label) == 0.0:
        label = "0"
    else:
        label = "1"

    new_line.append(label)

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = "%s:%s" % (i + 1, item)
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# ---

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    label_index = int(sys.argv[3])
except IndexError:
    label_index = 0  # Default to the first column as the label

skip_headers = sys.argv[4] if len(sys.argv) > 4 else 0  # Default to 0 if not provided

with open(input_file, 'r') as i, open(output_file, 'w') as o:
    reader = csv.reader(i)

    if skip_headers:
        next(reader)  # Skip header line if instructed

    for line in reader:
        if label_index == -1:
            label = '1'  # Default label if -1 is specified
        else:
            label = line.pop(label_index)

        new_line = construct_line(label, line)
        o.write(new_line)

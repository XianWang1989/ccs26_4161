
import sys
import csv

def construct_line(label, line):
    new_line = []
    if float(label) == 0.0:
        label = "0"
    new_line.append(label)

    for i, item in enumerate(line):
        if item.strip() == '' or float(item) == 0.0:
            continue
        new_item = "%s:%s" % (i + 1, item)
        new_line.append(new_item)
    new_line = " ".join(new_line)
    new_line += "\n"
    return new_line

# ---

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    label_index = int(sys.argv[3])
except IndexError:
    label_index = 0

skip_headers = False
if len(sys.argv) > 4 and sys.argv[4] == '1':
    skip_headers = True

with open(input_file, 'r', newline='') as i:
    reader = csv.reader(i)

    if skip_headers:
        next(reader)  # Skip the header row

    with open(output_file, 'w', newline='') as o:
        for line in reader:
            if label_index >= len(line):  # Ensure label index is valid
                print(f"Warning: Label index {label_index} is out of bounds for line: {line}")
                continue

            label = line.pop(label_index)
            new_line = construct_line(label, line)
            o.write(new_line)

print(f"Conversion complete! Output saved to {output_file}.")


import sys
import csv

def construct_line(label, line):
    new_line = []
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
    label_index = 0

try:
    skip_headers = int(sys.argv[4]) if len(sys.argv) > 4 else 0
except ValueError:
    skip_headers = 0

with open(input_file, 'r', newline='') as i:
    reader = csv.reader(i)

    if skip_headers:
        next(reader)  # Skip the header row if specified

    with open(output_file, 'w', newline='') as o:
        for line in reader:
            if line:  # Ensure line is not empty
                if label_index == -1:
                    label = '1'  # Assume a default label if not provided
                else:
                    label = line.pop(label_index)

                new_line = construct_line(label, line)
                o.write(new_line)

print(f"Conversion complete. Output saved to {output_file}.")

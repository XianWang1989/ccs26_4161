
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

# ---

input_file = sys.argv[1]
output_file = sys.argv[2]

# Default label index and skip headers flag
label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

with open(input_file, 'r') as i, open(output_file, 'w') as o:
    reader = csv.reader(i)

    # Skip headers if requested
    if skip_headers:
        next(reader)

    for line in reader:
        # Handle label assignment
        label = '1' if label_index == -1 else line.pop(label_index)
        new_line = construct_line(label, line)
        o.write(new_line)


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

# Input and output file handling
input_file = sys.argv[1]
output_file = sys.argv[2]
label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
skip_headers = sys.argv[4].lower() == 'true' if len(sys.argv) > 4 else False

with open(input_file, 'r') as i, open(output_file, 'w') as o:
    reader = csv.reader(i)

    if skip_headers:
        next(reader)  # Skip the header row

    for line in reader:
        label = line.pop(label_index) if label_index != -1 else '1'
        new_line = construct_line(label, line)
        o.write(new_line)

print("Conversion complete.")

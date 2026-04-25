
import sys
import csv

def construct_line(label, line):
    new_line = []
    # Handling the label
    if float(label) == 0.0:
        label = "0"
    new_line.append(label)

    # Constructing the LIBSVM formatted line
    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = "%s:%s" % (i + 1, item)
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# --- Main Execution ---

input_file = sys.argv[1]  # Input CSV file
output_file = sys.argv[2]  # Output LIBSVM file

# Default settings
label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

with open(input_file, 'r') as i:  # Open input CSV file
    reader = csv.reader(i)

    # Skip the headers if specified
    if skip_headers:
        headers = next(reader)

    with open(output_file, 'w') as o:  # Open output LIBSVM file
        for line in reader:
            if label_index == -1:
                label = '1'  # Default label if label_index is -1
            else:
                label = line.pop(label_index)

            new_line = construct_line(label, line)
            o.write(new_line)

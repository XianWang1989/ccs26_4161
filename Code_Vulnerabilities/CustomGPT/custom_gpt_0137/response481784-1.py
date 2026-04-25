
import sys
import csv

def construct_line(label, line):
    new_line = []
    if float(label) == 0.0:
        label = "0"  # LIBSVM expects labels to be strings
    new_line.append(label)

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue  # Skip any empty or zero-value features
        new_item = "%s:%s" % (i + 1, item)  # LIBSVM requires features in 1-based index format
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# Main conversion logic
if __name__ == "__main__":
    input_file = sys.argv[1]  # Input CSV file
    output_file = sys.argv[2]  # Output LIBSVM file

    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0  # Index of the label column
    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False  # Skip headers if needed

    with open(input_file, 'r') as i, open(output_file, 'w') as o:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)  # Skip the header row

        for line in reader:
            if label_index == -1:
                label = '1'  # Default label if no label index is provided
            else:
                label = line.pop(label_index)  # Remove label from the line

            new_line = construct_line(label, line)  # Convert to LIBSVM format
            o.write(new_line)  # Write to output file


import sys
import csv

def construct_line(label, line):
    new_line = []
    label = "0" if float(label) == 0.0 else label
    new_line.append(label)

    for i, item in enumerate(line):
        if item and float(item) != 0.0:  # Ignore empty and zero values
            new_item = f"{i + 1}:{item}"  # LIBSVM format
            new_line.append(new_item)

    return " ".join(new_line) + "\n"

def csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r', newline='') as i, open(output_file, 'w', newline='') as o:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)  # Skip the header

        for line in reader:
            if label_index == -1:  # If no label index is set
                label = '1'
            else:
                label = line.pop(label_index)

            new_line = construct_line(label, line)
            o.write(new_line)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Optional parameters with defaults
    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = sys.argv[4] == '1' if len(sys.argv) > 4 else False

    csv_to_libsvm(input_file, output_file, label_index, skip_headers)

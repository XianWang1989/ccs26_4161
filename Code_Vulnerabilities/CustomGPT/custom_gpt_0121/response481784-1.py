
import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(str(label))  # Ensure label is string

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# Main functionality
def convert_csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r', newline='') as i, open(output_file, 'w', newline='') as o:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)  # Skip header if present

        for line in reader:
            if label_index == -1:
                label = '1'  # Default label if not specified
            else:
                label = line.pop(label_index)

            new_line = construct_line(label, line)
            o.write(new_line)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

    convert_csv_to_libsvm(input_file, output_file, label_index, skip_headers)

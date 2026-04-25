
import sys
import csv

def construct_line(label, line):
    new_line = []

    # Ensure label is in string format
    new_line.append(str(int(label)) if label in ['0', 0] else str(label))

    for i, item in enumerate(line):
        if item == '' or float(item) == 0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

def csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        reader = csv.reader(infile)

        if skip_headers:
            next(reader)  # Skip header row

        for line in reader:
            if label_index < 0:
                label = '1'  # Default label
            else:
                label = line.pop(label_index)

            new_line = construct_line(label, line)
            outfile.write(new_line)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = sys.argv[4].lower() == 'true' if len(sys.argv) > 4 else False

    csv_to_libsvm(input_file, output_file, label_index, skip_headers)

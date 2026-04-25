
import csv
import sys

def construct_line(label, line):
    new_line = []
    new_line.append(label)  # Add the label first

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# Main function
def csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=0):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        reader = csv.reader(infile)

        if skip_headers:
            next(reader)  # Skip headers

        for line in reader:
            label = line.pop(label_index) if label_index != -1 else '1'
            new_line = construct_line(label, line)
            outfile.write(new_line)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = int(sys.argv[4]) if len(sys.argv) > 4 else 0

    csv_to_libsvm(input_file, output_file, label_index, skip_headers)


import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append("0" if float(label) == 0.0 else label)

    for i, item in enumerate(line):
        if item and float(item) != 0.0:
            new_item = f"{i + 1}:{item}"
            new_line.append(new_item)

    return " ".join(new_line) + "\n"

def convert_csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as i, open(output_file, 'w') as o:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)

        for line in reader:
            label = line.pop(label_index) if label_index != -1 else '1'
            new_line = construct_line(label, line)
            o.write(new_line)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

    convert_csv_to_libsvm(input_file, output_file, label_index, skip_headers)

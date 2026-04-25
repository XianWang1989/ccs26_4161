
import sys
import csv

def construct_line(label, line):
    new_line = [str(label)]
    for i, item in enumerate(line):
        if item.strip() == '' or float(item) == 0.0:  # Skip empty or zero items
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)
    return " ".join(new_line) + "\n"

def csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as i_file, open(output_file, 'w') as o_file:
        reader = csv.reader(i_file)

        if skip_headers:
            next(reader)  # Skip the header row

        for line in reader:
            if label_index < 0 or label_index >= len(line):
                label = '1'
            else:
                label = line.pop(label_index)

            new_line = construct_line(label, line)
            o_file.write(new_line)

if __name__ == "__main__":
    # Fetch command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

    csv_to_libsvm(input_file, output_file, label_index, skip_headers)

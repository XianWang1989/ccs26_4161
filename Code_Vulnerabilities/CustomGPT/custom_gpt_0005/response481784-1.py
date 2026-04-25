
import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(label if float(label) != 0.0 else "0")

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# Main function
def convert_csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        reader = csv.reader(infile)

        if skip_headers:
            next(reader)  # Skip header

        for line in reader:
            if label_index == -1:
                label = '1'
            else:
                label = line.pop(label_index)

            new_line = construct_line(label, line)
            outfile.write(new_line)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        label_index = int(sys.argv[3])
    except IndexError:
        label_index = 0

    try:
        skip_headers = bool(int(sys.argv[4]))
    except IndexError:
        skip_headers = False

    convert_csv_to_libsvm(input_file, output_file, label_index, skip_headers)

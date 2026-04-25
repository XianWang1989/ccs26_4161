
import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(label)  # Start with the label

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"  # Feature index starts at 1
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

def main(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as i, open(output_file, 'w') as o:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)  # Skip the header row

        for line in reader:
            label = line.pop(label_index)  # Get the label
            new_line = construct_line(label, line)  # Construct LIBSVM formatted line
            o.write(new_line)

if __name__ == "__main__":
    # Get command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Optional parameters
    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

    main(input_file, output_file, label_index, skip_headers)

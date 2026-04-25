
import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(label)  # LIBSVM format starts with label

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:  # Skip empty or zero features
            continue
        new_item = f"{i + 1}:{item}"  # Indexing starts from 1 in LIBSVM format
        new_line.append(new_item)

    return " ".join(new_line) + "\n"  # Join and return the new line

def main(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as i, open(output_file, 'w') as o:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)  # Skip the header row

        for line in reader:
            if label_index == -1:
                label = '1'  # Default label if none is specified
            else:
                label = line.pop(label_index)  # Pop the label from the line

            new_line = construct_line(label, line)
            o.write(new_line)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        label_index = int(sys.argv[3])
    except (IndexError, ValueError):
        label_index = 0  # Default label index

    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

    main(input_file, output_file, label_index, skip_headers)


import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(label)

    for i, item in enumerate(line):
        # Skip empty items and zero values
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

def main():
    if len(sys.argv) < 3:
        print("Usage: python csv_to_libsvm.py <input_file> <output_file> [label_index=0] [skip_headers=0]")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = int(sys.argv[4]) if len(sys.argv) > 4 else 0

    with open(input_file, 'r') as i_file, open(output_file, 'w') as o_file:
        reader = csv.reader(i_file)

        if skip_headers:
            next(reader)  # Skip header row

        for line in reader:
            if label_index == -1:
                label = '1'  # Default label if index is -1
            else:
                label = line.pop(label_index)  # Remove and get the label

            new_line = construct_line(label, line)
            o_file.write(new_line)

if __name__ == "__main__":
    main()


import sys
import csv

def construct_line(label, line):
    new_line = []
    # Ensure label is in string format
    if float(label) == 0.0:
        label = "0"
    new_line.append(label)

    # Construct feature indices and values
    for i, item in enumerate(line):
        # Skip empty items or items that convert to float 0.0
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

def main(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r', newline='', encoding='utf-8') as i:
        reader = csv.reader(i)

        # Skip headers if needed
        if skip_headers:
            next(reader)

        with open(output_file, 'w', newline='', encoding='utf-8') as o:
            for line in reader:
                # Remove label from the line if it's present
                if label_index == -1:
                    label = '1'  # Default for unlabeled
                else:
                    label = line.pop(label_index)

                new_line = construct_line(label, line)
                o.write(new_line)

if __name__ == "__main__":
    # Read arguments from the command line
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

    main(input_file, output_file, label_index, skip_headers)

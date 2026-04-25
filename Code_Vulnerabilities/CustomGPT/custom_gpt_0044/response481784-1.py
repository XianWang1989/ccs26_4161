
import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(str(label))  # Ensure label is a string

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"  # LIBSVM format
        new_line.append(new_item)

    new_line = " ".join(new_line) + "\n"
    return new_line

# Main block
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Optional parameters
    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = sys.argv[4].lower() == 'true' if len(sys.argv) > 4 else False

    with open(input_file, 'r') as i:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)  # Skip header row

        with open(output_file, 'w') as o:
            for line in reader:
                label = line.pop(label_index)  # Remove label from line
                new_line = construct_line(label, line)
                o.write(new_line)

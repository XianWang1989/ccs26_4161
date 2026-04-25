
import sys
import csv

def construct_line(label, line):
    new_line = []
    if float(label) == 0.0:
        label = "0"
    new_line.append(label)

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = "%s:%s" % (i + 1, item)
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# Main execution starts here
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        label_index = int(sys.argv[3])
    except (IndexError, ValueError):
        label_index = 0

    skip_headers = False
    if len(sys.argv) > 4 and sys.argv[4].lower() == 'true':
        skip_headers = True

    with open(input_file, 'r') as i, open(output_file, 'w') as o:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)  # Skip header row

        for line in reader:
            if label_index >= len(line) or label_index < 0:
                print("Label index out of range.")
                sys.exit(1)

            label = line.pop(label_index)  # Remove label from line
            new_line = construct_line(label, line)
            o.write(new_line)


import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(label)  # add the label to the start of the line
    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue  # skip empty or zero items
        new_item = f"{i + 1}:{item}"  # LIBSVM format (index:value)
        new_line.append(new_item)
    return " ".join(new_line) + "\n"

# Main execution
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        label_index = int(sys.argv[3])
    except IndexError:
        label_index = 0  # Default to the first column if not specified

    try:
        skip_headers = sys.argv[4].lower() == 'true'  # Check if headers should be skipped
    except IndexError:
        skip_headers = False

    with open(input_file, 'r') as i:
        reader = csv.reader(i)
        if skip_headers:
            next(reader)  # Skip header row if requested

        with open(output_file, 'w') as o:
            for line in reader:
                label = line.pop(label_index)  # Remove and get the label
                new_line = construct_line(label, line)
                o.write(new_line)

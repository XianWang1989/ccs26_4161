
import sys
import csv

def construct_line(label, line):
    new_line = []
    # Add label to the new line
    new_line.append(label)

    # Create key:value pairs for LIBSVM format
    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:  # Skip empty or zero items
            continue
        new_item = f"{i + 1}:{item}"  # LIBSVM format is "index:value"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"  # Return as a string with newline

def main(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as i, open(output_file, 'w') as o:
        reader = csv.reader(i)

        # Skip headers if specified
        if skip_headers:
            next(reader)

        for line in reader:
            if label_index == -1:
                label = '1'  # Default label if not specified
            else:
                label = line.pop(label_index)  # Remove and get the label

            # Construct the new LIBSVM formatted line
            new_line = construct_line(label, line)
            o.write(new_line)

if __name__ == "__main__":
    # Take command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Try to get optional arguments
    try:
        label_index = int(sys.argv[3])
    except (IndexError, ValueError):
        label_index = 0  # Default to 0 if not provided or invalid

    try:
        skip_headers = bool(int(sys.argv[4]))
    except (IndexError, ValueError):
        skip_headers = False  # Default to False if not provided or invalid

    main(input_file, output_file, label_index, skip_headers)

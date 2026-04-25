
import sys
import csv

def construct_line(label, line):
    new_line = [label]  # Start with the label
    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"  # Format features as index:value
        new_line.append(new_item)
    return " ".join(new_line) + "\n"

def main(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        reader = csv.reader(infile)

        if skip_headers:
            next(reader)  # Skip the header row

        for line in reader:
            if label_index < 0:
                label = '1'  # Default label if not provided
            else:
                label = line[label_index]  # Get the label

            line.pop(label_index)  # Remove the label from the feature set

            new_line = construct_line(label, line)  # Construct LIBSVM line
            outfile.write(new_line)  # Write to output file

if __name__ == "__main__":
    input_file = sys.argv[1]  # Input CSV file
    output_file = sys.argv[2]  # Output LIBSVM file
    try:
        label_index = int(sys.argv[3])  # Label column index
    except (IndexError, ValueError):
        label_index = 0  # Default label index

    try:
        skip_headers = sys.argv[4].lower() == 'true'  # Skip headers if specified
    except IndexError:
        skip_headers = False  # Default to not skip headers

    main(input_file, output_file, label_index, skip_headers)


import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(label)  # Add the label first

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"  # Create the LIBSVM format feature
        new_line.append(new_item)

    return " ".join(new_line) + "\n"  # Join the features and return

# Main execution block
if __name__ == "__main__":
    input_file = sys.argv[1]  # Input CSV file
    output_file = sys.argv[2]  # Output LIBSVM file
    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0  # Default label index
    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False  # Default to not skipping headers

    with open(input_file, 'r', newline='') as i, open(output_file, 'w', newline='') as o:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)  # Skip header line if indicated

        for line in reader:
            if label_index >= len(line):
                print(f"Warning: label_index {label_index} is out of range for line: {line}")
                continue

            label = line.pop(label_index)  # Extract the label
            new_line = construct_line(label, line)  # Transform the line
            o.write(new_line)  # Write to the output file

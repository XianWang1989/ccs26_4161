
import sys
import csv

def construct_line(label, features):
    """Construct a single LIBSVM format line from a label and feature list."""
    new_line = [str(label)]
    for index, value in enumerate(features):
        if value and float(value) != 0.0:  # Skip empty or zero values
            new_line.append(f"{index + 1}:{value}")
    return " ".join(new_line) + "\n"

def csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    """Convert a CSV file to LIBSVM format."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        reader = csv.reader(infile)

        if skip_headers:
            next(reader)  # Skip header row

        for line in reader:
            label = line.pop(label_index)  # Extract the label based on the index
            libsvm_line = construct_line(label, line)  # Construct LIBSVM line
            outfile.write(libsvm_line)  # Write to output file

if __name__ == "__main__":
    # Ensure proper command-line argument handling
    if len(sys.argv) < 3:
        print("Usage: python csv_to_libsvm.py <input_csv> <output_libsvm> [label_index] [skip_headers]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

    csv_to_libsvm(input_file, output_file, label_index, skip_headers)

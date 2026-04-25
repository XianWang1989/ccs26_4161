
import sys
import csv

def construct_line(label, line):
    """Construct line in LIBSVM format."""
    new_line = [str(int(label))]  # Convert label to integer if needed.

    for i, item in enumerate(line):
        if item and float(item) != 0.0:  # Skip empty and zero items.
            new_item = f"{i + 1}:{item}"  # LIBSVM format: index:value
            new_line.append(new_item)

    return " ".join(new_line) + "\n"

def csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    """Convert CSV to LIBSVM format."""
    with open(input_file, 'r', newline='') as i, open(output_file, 'w', newline='') as o:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)  # Skip header row if needed.

        for line in reader:
            label = line.pop(label_index) if label_index != -1 else '1'
            new_line = construct_line(label, line)
            o.write(new_line)

if __name__ == "__main__":
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

        csv_to_libsvm(input_file, output_file, label_index, skip_headers)
    except IndexError:
        print("Usage: python script.py <input_file> <output_file> [label_index] [skip_headers]")

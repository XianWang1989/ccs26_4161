
import sys
import csv

def construct_line(label, line):
    new_line = []
    # Ensure the label is in the right format
    new_line.append(str(label))

    for i, item in enumerate(line):
        # Skip empty or zero items
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"  # LIBSVM format requires 1-based index
        new_line.append(new_item)

    return " ".join(new_line) + "\n"  # Join the line and add newline

def main(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r', newline='', encoding='utf-8') as i:
        with open(output_file, 'w', newline='', encoding='utf-8') as o:
            reader = csv.reader(i)
            if skip_headers:
                next(reader)  # Skip header line if needed

            for line in reader:
                if label_index == -1:
                    label = '1'  # Default label if none is specified
                else:
                    label = line.pop(label_index)  # Remove and get the label

                new_line = construct_line(label, line)
                o.write(new_line)  # Write the formatted line to output file

if __name__ == "__main__":
    # Command line arguments: input_file, output_file, label_index, skip_headers
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

    main(input_file, output_file, label_index, skip_headers)

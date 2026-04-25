
import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(label)  # Add the label at the start

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue  # Skip empty or zero items
        new_item = f"{i + 1}:{item}"  # Format as index:value
        new_line.append(new_item)

    return " ".join(new_line) + "\n"  # Join and return the formatted string

def csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r', newline='') as i:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)  # Skip the header row

        with open(output_file, 'w') as o:
            for line in reader:
                if label_index == -1:
                    label = '1'  # Default label if none is specified
                else:
                    label = line.pop(label_index)  # Extract label based on index

                new_line = construct_line(label, line)
                o.write(new_line)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

    csv_to_libsvm(input_file, output_file, label_index, skip_headers)


import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(label)

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

def csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as i, open(output_file, 'w') as o:
        reader = csv.reader(i)

        if skip_headers:
            next(reader)  # Skip the header

        for line in reader:
            if label_index == -1:
                label = '1'  # Default label if not specified
            else:
                label = line.pop(label_index)

            new_line = construct_line(label, line)
            o.write(new_line)

# Example usage
if __name__ == "__main__":
    input_file = "testingset.csv"  # Path to your input CSV file
    output_file = "output.libsvm"   # Path to your desired output LIBSVM file
    csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=True)

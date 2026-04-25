
import sys
import csv

def construct_line(label, line):
    new_line = []
    # Ensure label is in the correct format
    new_line.append(label)

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = "%s:%s" % (i + 1, item)
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

def csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as i:
        reader = csv.reader(i)

        # Skip headers if needed
        if skip_headers:
            next(reader)

        with open(output_file, 'w') as o:
            for line in reader:
                if label_index == -1:
                    label = '1'
                else:
                    label = line.pop(label_index)
                    label = "1" if label.strip() == "1" else "0"

                new_line = construct_line(label, line)
                o.write(new_line)

# Example usage
if __name__ == "__main__":
    input_file = 'testingset.csv'
    output_file = 'output.libsvm'
    label_index = 0  # Change based on your CSV structure
    skip_headers = True  # Change to False if your CSV has no header

    csv_to_libsvm(input_file, output_file, label_index, skip_headers)

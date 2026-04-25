import sys
import csv

def construct_line(label, line):
    new_line = [str(int(float(label)))]  # Ensures label is integer string (e.g., '0' or '1')
    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_line.append(f"{i+1}:{item}")
    return " ".join(new_line) + "\n"

def csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r', newline='') as i, open(output_file, 'w', newline='') as o:
        reader = csv.reader(i)
        if skip_headers:
            next(reader)

        for line in reader:
            if label_index == -1:
                label = '1'
            else:
                label = line.pop(label_index)
            new_line = construct_line(label, line)
            o.write(new_line)

# Example usage:
# csv_to_libsvm('testingset.csv', 'output.libsvm', label_index=0, skip_headers=True)

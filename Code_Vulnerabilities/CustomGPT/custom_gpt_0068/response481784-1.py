
import sys
import csv

def construct_line(label, features):
    new_line = []
    if float(label) == 0.0:
        label = "0"
    new_line.append(label)

    for i, feature in enumerate(features):
        if feature == '' or float(feature) == 0.0:
            continue  # Skip empty and zero features
        new_item = f"{i + 1}:{feature}"  # LIBSVM format: index:value
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

def csv_to_libsvm(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        reader = csv.reader(infile)

        if skip_headers:
            next(reader)  # Skip header row if needed

        for line in reader:
            if label_index < len(line):
                label = line.pop(label_index)
            else:
                label = '1'  # Default to '1' if there's no label

            new_line = construct_line(label, line)
            outfile.write(new_line)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py input_file.csv output_file.txt [label_index] [skip_headers]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

    csv_to_libsvm(input_file, output_file, label_index, skip_headers)

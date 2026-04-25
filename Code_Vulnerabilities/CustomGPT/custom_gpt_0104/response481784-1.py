
import sys
import csv

def construct_line(label, line):
    new_line = []

    # LIBSVM specification requires label as a string
    new_line.append(str(int(label)))  # Ensure label is in string format

    for i, item in enumerate(line):
        if item.strip() == '' or float(item) == 0.0:
            continue
        new_item = "{}:{}".format(i + 1, item)
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    skip_headers = sys.argv[4] if len(sys.argv) > 4 else '0'

    with open(input_file, 'r', newline='', encoding='utf-8') as i, \
         open(output_file, 'w', newline='', encoding='utf-8') as o:

        reader = csv.reader(i)

        if skip_headers.lower() == '1':
            next(reader)  # Skip the header row if specified

        for line in reader:
            if label_index == -1:  # If label_index is -1, set label to 1
                label = '1'
            else:
                label = line.pop(label_index)

            new_line = construct_line(label, line)
            o.write(new_line)

if __name__ == "__main__":
    main()

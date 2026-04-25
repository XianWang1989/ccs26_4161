
import sys
import csv

def construct_line(label, line):
    new_line = []
    new_line.append(str(label))  # Convert label to string

    for i, item in enumerate(line):
        if item.strip() == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"  # Using f-string for better readability
        new_line.append(new_item)

    return " ".join(new_line) + "\n"

# ---

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        label_index = int(sys.argv[3])
    except IndexError:
        label_index = 0

    skip_headers = sys.argv[4] if len(sys.argv) > 4 else '0'
    skip_headers = int(skip_headers)

    with open(input_file, 'r') as i, open(output_file, 'w') as o:
        reader = csv.reader(i)

        # Skip headers if required
        if skip_headers:
            next(reader)

        for line in reader:
            if label_index == -1:
                label = '1'  # Default label if none specified
            else:
                label = line.pop(label_index)

            new_line = construct_line(label, line)
            o.write(new_line)

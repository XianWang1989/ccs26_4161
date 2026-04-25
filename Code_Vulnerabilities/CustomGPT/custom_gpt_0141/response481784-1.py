
import sys
import csv

def construct_line(label, line):
    new_line = []
    if float(label) == 0.0:
        label = "0"
    new_line.append(label)

    for i, item in enumerate(line):
        if item == '' or float(item) == 0.0:
            continue
        new_item = f"{i + 1}:{item}"
        new_line.append(new_item)

    new_line = " ".join(new_line) + "\n"
    return new_line

if __name__ == "__main__":
    # Input and output file paths
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Prepare to read the CSV file
    with open(input_file, 'r', newline='', encoding='utf-8') as i_file:
        reader = csv.reader(i_file)

        # Skip header if needed
        headers = next(reader, None)

        # Check which column is the label
        label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0

        with open(output_file, 'w', encoding='utf-8') as o_file:
            for line in reader:
                if label_index >= len(line):
                    print(f"Warning: Label index {label_index} is out of bounds for line: {line}")
                    continue

                label = line.pop(label_index)  # Remove the label from the line
                new_line = construct_line(label, line)
                o_file.write(new_line)

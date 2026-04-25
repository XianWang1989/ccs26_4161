
import sys
import csv

def construct_line(label, features):
    # Prepare the LIBSVM line format
    new_line = [label]
    for i, item in enumerate(features):
        if item and float(item) != 0.0:  # Avoid empty or zero features
            new_item = f"{i+1}:{item}"  # LIBSVM format requires 1-based indices
            new_line.append(new_item)
    return " ".join(new_line) + "\n"

def main(input_file, output_file, label_index=0, skip_headers=False):
    with open(input_file, 'r') as i:
        reader = csv.reader(i)

        # Skip the headers if required
        if skip_headers:
            next(reader)

        with open(output_file, 'w') as o:
            for line in reader:
                if label_index == -1:
                    label = '1'  # Default label
                else:
                    label = line.pop(label_index)

                # Construct LIBSVM line from the features
                new_line = construct_line(label, line)
                o.write(new_line)

if __name__ == "__main__":
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        label_index = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        skip_headers = bool(int(sys.argv[4])) if len(sys.argv) > 4 else False

        main(input_file, output_file, label_index, skip_headers)
    except IndexError:
        print("Usage: script.py <input_csv> <output_libsvm> [label_index=0] [skip_headers=0]")

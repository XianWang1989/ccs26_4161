
def count_lines_after(fname, target):
    with open(fname) as f:
        lines = f.readlines()

    # Find the line index of the target string
    try:
        target_index = lines.index(target + '\n')  # Add newline for exact match
    except ValueError:
        print(f"'{target}' not found in the file.")
        return 0  # Return 0 if the target line is not found

    # Count the lines after the target index
    return len(lines) - (target_index + 1)

# Usage
file_name = "test.ghx"
target_line = "{A   B}"
count = count_lines_after(file_name, target_line)
print(f"Number of lines after '{target_line}': {count}")

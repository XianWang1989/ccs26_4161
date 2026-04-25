
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Initialize a counter
    count = 0
    # Flag to indicate if the marker has been found
    found_marker = False

    for line in lines:
        if found_marker:
            count += 1
        elif marker in line:
            found_marker = True

    return count

# Usage
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker}': {line_count}")

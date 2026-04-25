
def count_lines_after_marker(fname, marker):
    line_count = 0
    found_marker = False

    with open(fname) as f:
        for line in f:
            # Check if the marker line is found
            if found_marker:
                line_count += 1
            if marker in line:
                found_marker = True

    return line_count

# Usage example
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker}':", line_count)

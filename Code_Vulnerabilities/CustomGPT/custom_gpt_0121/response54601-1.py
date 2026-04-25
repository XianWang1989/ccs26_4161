
def count_lines_after_marker(fname, marker):
    found_marker = False
    line_count = 0

    with open(fname) as f:
        for line in f:
            if marker in line:
                found_marker = True
                continue  # Skip the marker line
            if found_marker:
                line_count += 1

    return line_count

# Usage
marker = "{A   B}"
num_lines_after = count_lines_after_marker("test.ghx", marker)
print(num_lines_after)


def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        found_marker = False
        line_count = 0

        for line in f:
            if found_marker:
                line_count += 1
            elif marker in line:
                found_marker = True

    return line_count

# Usage example
marker = "{A   B}"
num_lines = count_lines_after_marker("test.ghx", marker)
print(num_lines)

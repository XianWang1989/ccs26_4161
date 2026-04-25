
def count_lines_after_marker(fname, marker):
    after_marker = False
    line_count = 0

    with open(fname) as f:
        for line in f:
            if marker in line:
                after_marker = True
                continue  # Skip the line with the marker

            if after_marker:
                line_count += 1

    return line_count

# Usage
count = count_lines_after_marker("test.ghx", "{A   B}")
print("Number of lines after '{A   B}':", count)

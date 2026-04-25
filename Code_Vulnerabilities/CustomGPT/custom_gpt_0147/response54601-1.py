
def count_lines_after_marker(fname, marker):
    count = 0
    found_marker = False

    with open(fname) as f:
        for line in f:
            if marker in line:
                found_marker = True
            elif found_marker:
                count += 1

    return count

# Usage
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(f'Number of lines after {marker}: {line_count}')

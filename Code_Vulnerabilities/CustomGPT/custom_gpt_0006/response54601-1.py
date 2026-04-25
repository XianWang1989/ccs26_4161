
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        found_marker = False
        line_count = 0

        for line in f:
            if found_marker:
                line_count += 1
            if marker in line:
                found_marker = True

    return line_count

# Example usage
marker = '{A   B}'
count_after = count_lines_after_marker("test.ghx", marker)
print(count_after)

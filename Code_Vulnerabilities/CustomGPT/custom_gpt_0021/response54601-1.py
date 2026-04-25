
def count_lines_after_marker(fname, marker):
    with open(fname, 'r') as f:
        lines_after_marker = 0
        found_marker = False

        for line in f:
            if found_marker:
                lines_after_marker += 1
            elif marker in line:
                found_marker = True

    return lines_after_marker

# Example usage
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(line_count)


def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        line_found = False
        line_count = 0

        for line in f:
            if line_found:
                line_count += 1
            if marker in line:
                line_found = True

    return line_count

# Example usage
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker}': {line_count}")

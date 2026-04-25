
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        line_found = False
        line_count = 0

        for line in f:
            if line.strip() == marker:
                line_found = True  # Mark that we've found the line
            elif line_found:
                line_count += 1  # Increase count for lines after the marker

    return line_count

# Example usage
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker}': {line_count}")

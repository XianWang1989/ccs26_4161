
def count_lines_after_marker(fname, marker):
    found_marker = False
    line_count = 0

    with open(fname) as f:
        for line in f:
            if found_marker:
                line_count += 1  # Increment the line count after the marker is found
            elif marker in line:
                found_marker = True  # Found the marker; start counting after this line

    return line_count

# Example usage
file_name = "test.ghx"
marker = "{A   B}"
lines_after_marker = count_lines_after_marker(file_name, marker)
print(f"Number of lines after '{marker}': {lines_after_marker}")

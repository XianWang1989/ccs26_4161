
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        # Initialize variables
        line_count = 0
        marker_found = False

        for line in f:
            if marker_found:
                line_count += 1  # Increment the count for each line after the marker
            elif marker in line:
                marker_found = True  # Mark that we found the specific line

    return line_count

# Example usage
filename = "test.ghx"
marker = "{A   B}"
count = count_lines_after_marker(filename, marker)
print(f"Number of lines after '{marker}': {count}")

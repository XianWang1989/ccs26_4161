
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        # Initialize the counter and a flag
        count = 0
        marker_found = False

        for line in f:
            # Check if the marker is found
            if marker_found:
                count += 1  # Count lines after the marker
            if marker in line:
                marker_found = True  # Mark that we found the marker

    return count

# Usage example
file_path = "test.ghx"
marker = "{A   B}"
lines_after_marker = count_lines_after_marker(file_path, marker)
print(lines_after_marker)


def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the marker line
    try:
        marker_index = lines.index(marker + '\n')  # Adjust for line endings
        # Count lines after the marker
        return len(lines) - (marker_index + 1)
    except ValueError:
        print("Marker not found.")
        return 0

# Usage
marker_line = '{A   B}'
line_count = count_lines_after_marker("test.ghx", marker_line)
print(f"Number of lines after '{marker_line}': {line_count}")

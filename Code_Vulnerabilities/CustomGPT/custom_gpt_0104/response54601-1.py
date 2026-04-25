
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the line containing the marker
    try:
        marker_index = lines.index(marker)  # Get the index of the marker line
        # Count the number of lines after the marker
        count = len(lines) - (marker_index + 1)
        return count
    except ValueError:
        return 0  # Marker not found in the file

# Usage
marker = "{A   B}\n"  # Include the newline character if the line ends with it
line_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker.strip()}': {line_count}")

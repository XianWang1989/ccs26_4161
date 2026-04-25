
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Identify the position of the marker
    if marker in lines:
        # Count lines after the marker
        marker_index = lines.index(marker)
        return len(lines) - (marker_index + 1)
    else:
        return 0  # Marker not found

# Example usage
marker = "{A   B}\n"
line_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker.strip()}': {line_count}")

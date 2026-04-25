
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the marker
    try:
        marker_index = lines.index(marker + '\n')  # Include newline character
    except ValueError:
        return 0  # Marker not found

    # Count lines after the marker
    return len(lines) - marker_index - 1  # Subtract one for the marker line itself

# Example usage
file_name = "test.ghx"
marker = "{A   B}"
line_count = count_lines_after_marker(file_name, marker)
print(f"Number of lines after '{marker}': {line_count}")


def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the marker
    try:
        marker_index = lines.index(marker + '\n')  # Including newline character
        return len(lines) - (marker_index + 1)  # Count lines after the marker
    except ValueError:
        return 0  # Marker not found

# Example usage
file_name = "test.ghx"
marker = "{A   B}"
lines_after = count_lines_after_marker(file_name, marker)
print(f"Number of lines after '{marker}': {lines_after}")

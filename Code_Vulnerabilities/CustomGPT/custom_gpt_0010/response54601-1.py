
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list.

    if marker in lines:
        start_index = lines.index(marker) + 1  # Find the marker and start counting after it.
        return len(lines) - start_index  # Count lines after the marker.
    else:
        return 0  # Return 0 if the marker is not found.

# Example usage
marker = "{A   B}\n"  # Ensure the marker matches exactly, including new line.
line_count = count_lines_after_marker("test.ghx", marker)
print(line_count)


def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines

    # Find the index of the marker line
    try:
        marker_index = lines.index(marker + '\n')  # Adjust for newline character
        return len(lines) - marker_index - 1  # Count lines after the marker
    except ValueError:
        return 0  # Return 0 if the marker isn't found

# Usage example
file_name = "test.ghx"
marker = "{A   B}"
count = count_lines_after_marker(file_name, marker)
print(f"Number of lines after '{marker}': {count}")

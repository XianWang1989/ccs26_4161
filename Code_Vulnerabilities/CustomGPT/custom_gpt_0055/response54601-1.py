
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list
        try:
            marker_index = lines.index(marker + '\n')  # Find the index of the marker line
            return len(lines) - (marker_index + 1)  # Count lines after the marker
        except ValueError:
            return 0  # Return 0 if the marker is not found

# Example usage
filename = "test.ghx"
marker = "{A   B}"
line_count = count_lines_after_marker(filename, marker)
print(f"Number of lines after '{marker}': {line_count}")

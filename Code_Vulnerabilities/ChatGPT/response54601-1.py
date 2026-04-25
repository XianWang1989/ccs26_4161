
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines at once
        try:
            # Find the index of the line containing the marker
            marker_index = lines.index(marker + '\n')
            # Count lines after the marker
            lines_after_marker = lines[marker_index + 1:]  # Get lines after the marker
            return len(lines_after_marker)  # Return the count of those lines
        except ValueError:
            # Marker not found
            print(f"Marker '{marker}' not found in the file.")
            return 0 

# Example usage
marker = "{A   B}"
count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker}': {count}")

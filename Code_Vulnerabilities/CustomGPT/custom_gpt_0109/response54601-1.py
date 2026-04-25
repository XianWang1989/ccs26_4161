
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list
        # Find the index of the marker
        if marker in lines:
            marker_index = lines.index(marker)
            # Count lines after the marker
            return len(lines) - marker_index - 1
        else:
            return 0  # Return 0 if marker is not found

# Example usage
marker = "{A   B}\n"  # Ensure to include the newline character
count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker.strip()}': {count}")


def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list
        # Find the index of the marker
        try:
            marker_index = lines.index(marker + '\n')  # Include newline character
            # Count the lines after the marker
            count_after = len(lines) - (marker_index + 1)
            return count_after
        except ValueError:
            print("Marker not found in the file.")
            return 0

# Example usage
file_name = "test.ghx"
marker = "{A   B}"
count = count_lines_after_marker(file_name, marker)
print(f"Number of lines after '{marker}': {count}")

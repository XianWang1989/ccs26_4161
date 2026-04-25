
def count_lines_after_marker(fname, marker):
    with open(fname, 'r') as f:
        count = 0
        found_marker = False

        for line in f:
            if found_marker:
                count += 1  # Increment count after the marker is found
            elif marker in line:
                found_marker = True  # Mark that the marker line has been found

        return count

# Example usage
marker_line = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker_line)
print("Number of lines after the marker line:", line_count)

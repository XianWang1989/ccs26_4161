
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        # Initialize a flag and line count
        counting = False
        line_count = 0

        for line in f:
            if marker in line:
                counting = True  # Start counting after finding the marker
                continue  # Skip the marker line
            if counting:
                line_count += 1  # Count subsequent lines

    return line_count

# Example usage
marker = "{A   B}"
num_lines_after = count_lines_after_marker("test.ghx", marker)
print(num_lines_after)


def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        # Initialize a counter for lines after the marker
        count_after_marker = 0
        found_marker = False

        for line in f:
            # Check if the marker line is found
            if marker in line:
                found_marker = True
                continue  # Skip the marker line

            # If the marker has been found, increase the count
            if found_marker:
                count_after_marker += 1

    return count_after_marker

# Usage
marker = "{A   B}"
lines_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker}': {lines_count}")

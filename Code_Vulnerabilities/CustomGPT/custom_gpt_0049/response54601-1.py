
def count_lines_after_marker(fname, marker='{A   B}'):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list
        count = 0
        marker_found = False

        for line in lines:
            if marker_found:
                count += 1  # Increment count for every line after the marker
            if marker in line:
                marker_found = True  # Set the marker found flag

        return count

# Usage
num_lines = count_lines_after_marker("test.ghx")
print(num_lines)

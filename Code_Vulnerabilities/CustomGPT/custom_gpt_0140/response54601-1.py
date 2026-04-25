
def count_lines_after_marker(fname, marker):
    count = 0
    found_marker = False

    with open(fname) as f:
        for line in f:
            if found_marker:
                count += 1
            if marker in line:
                found_marker = True

    return count

# Example usage
filename = "test.ghx"
marker = "{A   B}"
lines_after = count_lines_after_marker(filename, marker)
print(f"Number of lines after '{marker}': {lines_after}")

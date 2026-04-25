
def count_lines_after_marker(fname, marker):
    with open(fname, 'r') as f:
        reached_marker = False
        line_count = 0

        for line in f:
            if reached_marker:
                line_count += 1
            elif marker in line:
                reached_marker = True

    return line_count

# Example usage
file_name = "test.ghx"
marker = "{A   B}"
lines_after = count_lines_after_marker(file_name, marker)
print(f"Number of lines after '{marker}': {lines_after}")

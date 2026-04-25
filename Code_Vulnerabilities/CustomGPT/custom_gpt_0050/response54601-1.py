
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        count = 0
        found = False

        for line in f:
            if found:
                count += 1
            if marker in line:
                found = True

    return count

# Usage example:
file_name = "test.ghx"
marker = "{A   B}"
lines_count = count_lines_after_marker(file_name, marker)
print(lines_count)

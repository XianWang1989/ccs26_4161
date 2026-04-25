
def count_lines_after_marker(filename, marker):
    with open(filename) as f:
        count = 0
        found_marker = False

        for line in f:
            if found_marker:
                count += 1
            if marker in line:
                found_marker = True

    return count

# Usage
filename = "test.ghx"
marker = "{A   B}"
lines_count = count_lines_after_marker(filename, marker)
print(lines_count)

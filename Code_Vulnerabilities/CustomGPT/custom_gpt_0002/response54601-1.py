
def count_lines_after_specific_line(fname, specific_line):
    with open(fname) as f:
        found = False
        count = 0
        for line in f:
            if found:
                count += 1
            if specific_line in line:
                found = True
        return count

# Usage
line_count = count_lines_after_specific_line("test.ghx", "{A   B}")
print(line_count)

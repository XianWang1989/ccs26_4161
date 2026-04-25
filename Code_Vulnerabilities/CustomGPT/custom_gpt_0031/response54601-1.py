
def count_lines_after_specific_line(fname, specific_line):
    line_count = 0
    found = False

    with open(fname) as f:
        for line in f:
            if found:
                line_count += 1
            if line.strip() == specific_line:
                found = True

    return line_count

# Use the function
specific_line = "{A   B}"
line_count = count_lines_after_specific_line("test.ghx", specific_line)
print(line_count)

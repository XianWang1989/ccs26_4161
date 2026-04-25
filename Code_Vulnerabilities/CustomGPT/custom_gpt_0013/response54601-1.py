
def count_lines_after_specific_line(fname, search_text):
    found = False
    line_count = 0

    with open(fname) as f:
        for line in f:
            if found:
                line_count += 1
            if search_text in line:
                found = True

    return line_count

# Usage example
line_count = count_lines_after_specific_line("test.ghx", "{A   B}")
print(line_count)

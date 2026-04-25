
def count_lines_after_specific_line(fname, specific_line):
    found = False
    line_count = 0

    with open(fname) as f:
        for line in f:
            if found:
                line_count += 1
            elif specific_line in line:
                found = True

    return line_count

# Example usage
specific_line = "{A   B}"  # The line you are looking for
count = count_lines_after_specific_line("test.ghx", specific_line)
print(count)


def count_lines_after_keyword(fname, keyword):
    with open(fname) as f:
        found_keyword = False
        line_count = 0

        for line in f:
            if found_keyword:
                line_count += 1
            if keyword in line:
                found_keyword = True

    return line_count

# Replace 'test.ghx' with your file name
line_count = count_lines_after_keyword("test.ghx", "{A   B}")
print("Number of lines after {A   B}:", line_count)

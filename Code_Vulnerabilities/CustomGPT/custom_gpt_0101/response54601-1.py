
def count_lines_after_keyword(fname, keyword):
    with open(fname) as f:
        lines = f.readlines()

    count = 0
    found_keyword = False

    for line in lines:
        if found_keyword:
            count += 1
        if keyword in line:
            found_keyword = True

    return count

# Usage
lines_count = count_lines_after_keyword("test.ghx", "{A   B}")
print(lines_count)

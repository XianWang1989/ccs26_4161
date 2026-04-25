
def count_lines_after_keyword(fname, keyword):
    count = 0
    found = False

    with open(fname) as f:
        for line in f:
            if found:
                count += 1
            elif keyword in line:
                found = True

    return count

# Usage
filename = "test.ghx"
keyword = "{A   B}"
line_count = count_lines_after_keyword(filename, keyword)
print(f"Number of lines after '{keyword}': {line_count}")

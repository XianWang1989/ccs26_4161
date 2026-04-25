
def count_lines_after_keyword(fname, keyword):
    with open(fname) as f:
        line_found = False
        count = 0

        for line in f:
            if line_found:
                count += 1
            if keyword in line:
                line_found = True

    return count

# Usage example
filename = "test.ghx"
keyword = "{A   B}"
line_count = count_lines_after_keyword(filename, keyword)
print(f"Number of lines after '{keyword}': {line_count}")

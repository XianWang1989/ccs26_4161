
def count_lines_after_keyword(fname, keyword):
    with open(fname) as f:
        count = 0
        found_keyword = False

        for line in f:
            if found_keyword:
                count += 1
            if keyword in line:
                found_keyword = True

    return count

# Example usage
filename = "test.ghx"
keyword = "{A   B}"
line_count = count_lines_after_keyword(filename, keyword)
print(line_count)

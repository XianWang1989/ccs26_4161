def count_lines_after_keyword(fname, keyword):
    with open(fname, 'r') as f:
        found_keyword = False
        line_count = 0
        for line in f:
            if found_keyword:
                line_count += 1
            if keyword in line:
                found_keyword = True
        return line_count

# Example usage
fname = "test.ghx"
keyword = "{A   B}"
print(count_lines_after_keyword(fname, keyword))

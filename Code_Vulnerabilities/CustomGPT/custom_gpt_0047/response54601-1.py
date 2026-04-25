
def count_lines_after_keyword(fname, keyword):
    lines_after = 0
    found_keyword = False

    with open(fname, 'r') as f:
        for line in f:
            if found_keyword:  
                lines_after += 1
            if keyword in line:  
                found_keyword = True  

    return lines_after

# Example usage
filename = "test.ghx"
keyword = "{A   B}"
line_count = count_lines_after_keyword(filename, keyword)
print(f"Number of lines after '{keyword}': {line_count}")

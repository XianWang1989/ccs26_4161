
def count_lines_after_keyword(fname, keyword):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list

    count = 0
    found_keyword = False

    for line in lines:
        if found_keyword:  # If the keyword has been found, count this line
            count += 1
        if keyword in line:  # Check if the current line contains the keyword
            found_keyword = True  # Set the flag to True after finding the keyword

    return count

# Example usage
file_name = "test.ghx"
keyword = "{A   B}"
line_count = count_lines_after_keyword(file_name, keyword)
print(f"Number of lines after '{keyword}': {line_count}")

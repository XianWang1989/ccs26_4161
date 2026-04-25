
def count_lines_after_keyword(fname, keyword):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the line containing the keyword
    for index, line in enumerate(lines):
        if keyword in line:
            # Count lines after the found index
            return len(lines) - index - 1  # Exclude the line with the keyword

    return 0  # Return 0 if the keyword is not found

# Example usage
filename = "test.ghx"
keyword = "{A   B}"
count = count_lines_after_keyword(filename, keyword)
print(f"Number of lines after '{keyword}': {count}")

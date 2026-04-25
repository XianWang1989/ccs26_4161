
def count_lines_after_keyword(filename, keyword):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Find the index of the line containing the keyword
    for index, line in enumerate(lines):
        if keyword in line:
            # Count lines after the keyword line
            return len(lines) - (index + 1)

    return 0  # Return 0 if the keyword is not found

# Usage
filename = "test.ghx"
keyword = "{A   B}"
lines_after = count_lines_after_keyword(filename, keyword)

print(f"Number of lines after '{keyword}': {lines_after}")

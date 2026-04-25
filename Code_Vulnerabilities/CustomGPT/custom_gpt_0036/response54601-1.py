
def count_lines_after_keyword(fname, keyword):
    with open(fname) as f:
        # Initialize a counter
        line_count = 0
        found_keyword = False

        # Iterate through each line in the file
        for line in f:
            # Check if the keyword is found in the line
            if keyword in line:
                found_keyword = True
                continue  # Skip the line with the keyword

            # If the keyword has been found, increment the line counter
            if found_keyword:
                line_count += 1

    return line_count

# Use the function
filename = "test.ghx"
keyword = "{A   B}"
lines_after = count_lines_after_keyword(filename, keyword)
print(f"Number of lines after '{keyword}': {lines_after}")

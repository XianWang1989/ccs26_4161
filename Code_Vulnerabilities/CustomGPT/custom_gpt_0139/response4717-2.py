
all_processed_lines = []

with open('reg.fa', 'r') as fh:
    for line in fh:
        processed_line = line.strip()
        all_processed_lines.append(processed_line)

# Now you can do something with all_processed_lines, e.g., joining them in a single string
result_string = '\n'.join(all_processed_lines)
print(result_string)

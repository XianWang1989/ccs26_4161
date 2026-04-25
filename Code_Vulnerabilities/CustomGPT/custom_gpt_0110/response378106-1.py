
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        current_position = self.f.tell()

        # Move to the start and read lines
        self.f.seek(0)
        line_count = 0
        position_in_line = 0

        while True:
            line = self.f.readline()
            if not line:  # End of file
                break

            # Check if the current position is within the length of this line
            if current_position >= position_in_line + len(line):
                position_in_line += len(line)
                line_count += 1
            else:
                break

        # Restore the file pointer to the initial position
        self.f.seek(current_position)

        # Return based on char flag
        if char:
            return line_count, current_position - position_in_line
        return line_count

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')

# Add some lines (for testing purposes)
editor.f.write("First line\nSecond line\nThird line\n")
editor.f.flush()

# Now use tell() to find the line number
editor.f.seek(0)  # Reset pointer to read all lines
line_number = editor.tell()
print(f"Current line number: {line_number}")

# Close the file
editor.close()

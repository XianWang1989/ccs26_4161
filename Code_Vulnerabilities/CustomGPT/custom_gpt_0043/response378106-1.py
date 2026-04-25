
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Get the current file position
        line_count = 0
        current_position = 0

        # Use a separate seek to reset the file pointer for iteration
        self.f.seek(0)

        while True:
            line = self.f.readline()  # Read one line
            if not line:  # Stop if it's EOF
                break
            line_length = len(line)  # Get line length
            if current_position + line_length > t:
                # We've found the line that the cursor is on
                break
            current_position += line_length
            line_count += 1

        # Return the character position if requested
        if char:
            return line_count, t - current_position
        return line_count

    def close(self):
        self.f.close()

# Example usage:
editor = FileEditor('example.txt')

# Don't forget to open the file and write something before testing tell
editor.f.write("This is line 1.\n")
editor.f.write("This is line 2.\n")
editor.f.write("This is line 3.\n")
editor.f.flush()  # Ensure the content is written to the file

# Move the cursor to a specific position and test tell
editor.f.seek(20)  # For example, position it in the middle of line 2
print(editor.tell())  # Output would be based on current position
print(editor.tell(char=True))  # Output would include line count and char offset

editor.close()

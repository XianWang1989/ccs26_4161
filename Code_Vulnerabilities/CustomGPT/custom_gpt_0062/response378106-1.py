
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        current_pos = self.f.tell()

        # Move to the beginning of the file
        self.f.seek(0)

        # Initialize line count and position tracking
        line_count = 0
        char_position = 0

        # Read through the file to count lines and track char position
        for line in self.f:
            line_length = len(line)
            if current_pos >= char_position + line_length:
                char_position += line_length
                line_count += 1
            else:
                break

        # Restore the original position
        self.f.seek(current_pos)

        # Return the count or both count and char position
        if char:
            return line_count, current_pos - char_position
        return line_count

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print(editor.tell())  # Get the line number of the current position
print(editor.tell(char=True))  # Get line number and char offset
editor.close()

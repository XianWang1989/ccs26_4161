
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        current_position = self.f.tell()
        line_count = 0

        # Seek back to the start of the file to iterate
        self.f.seek(0)

        # Temporary variable to keep track of characters read
        char_offset = 0

        for line in self.f:
            line_length = len(line)
            if current_position >= char_offset + line_length:
                # Move to the next line
                char_offset += line_length
                line_count += 1
            else:
                # We've found the line containing the original pos
                break

        # Return character data if requested
        if char:
            return line_count, current_position - char_offset
        return line_count

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
editor.f.write("This is the first line.\n")
editor.f.write("This is the second line.\n")
editor.f.write("This is the third line.\n")
editor.f.seek(0)  # Reset the cursor to the start for the tell test
line, char = editor.tell(char=True)
print(f"Position: Line {line}, Character Offset {char}")
editor.close()

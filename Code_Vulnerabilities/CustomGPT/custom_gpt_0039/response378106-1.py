
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()
        line_count = 0
        char_position = 0

        # Reset the file pointer to the beginning to count lines
        self.f.seek(0)

        for line in self.f:
            line_length = len(line)
            if current_position >= char_position + line_length:
                char_position += line_length
                line_count += 1
            else:
                break

        # Return character position if required
        if char:
            return line_count, current_position - char_position
        return line_count

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print("Line count:", editor.tell())  # Returns number of lines up to the current position
print("Line count with char:", editor.tell(char=True))  # Returns line count and character position
editor.close()

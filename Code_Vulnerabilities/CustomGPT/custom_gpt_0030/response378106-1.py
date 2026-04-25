
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        position = self.f.tell()  # Get the current position
        line_count = 0
        char_count = 0

        # Save the current position to restore later
        current_position = self.f.tell()

        # Go to the start of the file to count lines
        self.f.seek(0)

        # Count lines and calculate character count up to the original position
        for line in self.f:
            if current_position >= char_count + len(line):
                char_count += len(line)
                line_count += 1
            else:
                break

        # Restore the original position
        self.f.seek(current_position)

        if char:
            return line_count, position - char_count
        return line_count

    def close(self):
        self.f.close()

# Example usage
editor = FileEditor('example.txt')
print(editor.tell())  # Get line count
print(editor.tell(char=True))  # Get line count and position in characters
editor.close()

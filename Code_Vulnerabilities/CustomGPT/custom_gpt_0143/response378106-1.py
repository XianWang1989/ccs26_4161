
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()  # Store the current position
        self.f.seek(0)  # Move to the start of the file
        line_count = 0
        remaining_bytes = current_position

        for line in self.f:
            if remaining_bytes >= len(line):
                remaining_bytes -= len(line)
                line_count += 1
            else:
                break

        self.f.seek(current_position)  # Restore to the original position

        if char:
            return line_count, remaining_bytes
        return line_count

    def close(self):
        self.f.close()

# Example usage:
editor = FileEditor('example.txt')
print(editor.tell())  # Outputs the line count and potentially remaining bytes
editor.close()

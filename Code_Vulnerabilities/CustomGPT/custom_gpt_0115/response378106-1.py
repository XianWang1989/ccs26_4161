
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Store the current position
        current_position = self.f.tell()

        # Restart reading from the beginning
        self.f.seek(0)
        line_count = 0
        line_position = current_position

        for line in self.f:
            line_length = len(line)
            if line_position >= line_length:
                line_position -= line_length
                line_count += 1
            else:
                break

        # Reset the cursor back to the original position
        self.f.seek(current_position)

        return (line_count, line_position) if char else line_count

    def close(self):
        self.f.close()

# Example usage
with FileEditor('example.txt') as editor:
    # Write something to the file for demonstration
    editor.f.write("First line\nSecond line\nThird line\n")

    # Use the tell function
    print(editor.tell())  # Should print the number of lines

# Remember to close the file when done or use a context manager

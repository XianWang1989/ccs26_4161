
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Create a Unicode string
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the Unicode string directly
print(docText)

# If you need to write to a UTF-8 file
with open('output.txt', 'w') as f:
    f.write(docText.encode('utf-8'))


import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs without encoding to UTF-8
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly (in Python 2, this should work without explicit decode)
print docText

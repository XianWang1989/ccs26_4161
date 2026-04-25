
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect all paragraphs as Unicode strings
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Now, simply print the docText. Avoid decoding if not necessary.
print(docText)

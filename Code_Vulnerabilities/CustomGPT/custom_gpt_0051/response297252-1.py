
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs as a Unicode string
docText = u'\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Now print the Unicode string directly
print(docText)

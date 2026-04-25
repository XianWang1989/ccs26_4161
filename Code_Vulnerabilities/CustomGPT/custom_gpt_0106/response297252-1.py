
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs into a single Unicode string
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the Unicode text directly
print(docText)

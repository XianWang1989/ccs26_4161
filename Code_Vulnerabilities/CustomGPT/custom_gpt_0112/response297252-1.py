
import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs into a single Unicode string
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the Unicode string directly
print docText

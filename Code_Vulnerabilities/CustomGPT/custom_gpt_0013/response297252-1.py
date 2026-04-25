
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Join paragraphs without encoding
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# If you need to handle special characters, keep the text as is
print docText  # This should work with special characters directly

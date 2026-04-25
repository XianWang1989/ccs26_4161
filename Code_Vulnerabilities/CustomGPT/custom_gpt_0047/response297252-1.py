
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect text with proper encoding
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text (no need to decode since it's already unicode)
print docText

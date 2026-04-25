
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect text with proper encoding
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the text
print(docText)

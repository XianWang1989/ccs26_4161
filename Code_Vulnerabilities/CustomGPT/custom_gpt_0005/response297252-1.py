
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect text from paragraphs
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly without encoding
print docText.encode('utf-8')

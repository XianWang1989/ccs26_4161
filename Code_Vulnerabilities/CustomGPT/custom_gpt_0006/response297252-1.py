
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect text with proper encoding handling
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the text directly, as it remains a Unicode string in Python 2.7
print(docText)

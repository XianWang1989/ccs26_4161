
import sys
import docx

# Read the document
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Ensure proper stdout encoding
sys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8', errors='replace')

# Print the text
print(docText)

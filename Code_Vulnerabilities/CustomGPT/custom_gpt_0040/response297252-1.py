
import docx
import sys

# Set the proper encoding for output
reload(sys)
sys.setdefaultencoding('utf-8')

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')

# Collect text from paragraphs and join them with double newlines
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the document text directly
print(docText.encode('utf-8'))

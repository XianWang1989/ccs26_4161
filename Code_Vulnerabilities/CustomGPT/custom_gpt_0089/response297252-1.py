
import docx
import sys

# Set the default encoding to handle UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')

# Read the document
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text, ensuring proper encoding
print docText.encode('utf-8')  # Use encode() when printing

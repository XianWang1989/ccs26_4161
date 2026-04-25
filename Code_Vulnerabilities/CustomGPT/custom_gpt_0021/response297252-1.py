
import docx
import sys

# Set the encoding to handle special characters
reload(sys)
sys.setdefaultencoding('utf-8')

# Load the document
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the document text
print docText

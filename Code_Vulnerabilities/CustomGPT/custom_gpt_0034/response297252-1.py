
import docx
import sys

# Set the encoding for the console, if necessary
reload(sys)
sys.setdefaultencoding('utf-8')

# Read the document
document = docx.Document('sim_dir_administrativo.docx')
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text
print docText  # No need to decode if it's already a Unicode string

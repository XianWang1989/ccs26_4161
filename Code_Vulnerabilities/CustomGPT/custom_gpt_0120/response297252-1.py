
import docx
import sys

# Set the default encoding to utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Create the text from paragraphs
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the output directly as a UTF-8 string
print docText

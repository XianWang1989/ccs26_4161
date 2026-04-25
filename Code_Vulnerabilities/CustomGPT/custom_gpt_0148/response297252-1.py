
import docx
import sys

# Set the standard output encoding to UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')

document = docx.Document('sim_dir_administrativo.docx')

# Create a UTF-8 encoded string
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text as UTF-8 encoded
print docText.encode('utf-8')

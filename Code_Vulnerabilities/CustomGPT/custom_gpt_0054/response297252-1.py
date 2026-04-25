
import docx
import sys

# Ensure the default encoding is set to UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text
print docText


import docx
import sys

# Set the default encoding to UTF-8 for the terminal
reload(sys)
sys.setdefaultencoding('utf-8')

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Combine paragraphs into a single Unicode string
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the output directly without decoding
print(docText)

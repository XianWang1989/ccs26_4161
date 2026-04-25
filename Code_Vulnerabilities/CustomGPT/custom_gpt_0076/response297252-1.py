
import docx
import sys

# Set the default encoding to UTF-8
reload(sys)
sys.setdefaultencoding('utf-8')

# Read the document
document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs  # No encode needed here
])

# Print the text directly
print(docText)  # No need to decode since it's already a Unicode string

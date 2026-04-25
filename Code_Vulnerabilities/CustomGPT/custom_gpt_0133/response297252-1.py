
import docx
import sys

# Set the default encoding to utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Create docText with safely encoded text
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the docText
# If you are using a console that doesn't support utf-8,
# You might want to encode when printing
print docText.encode('utf-8')

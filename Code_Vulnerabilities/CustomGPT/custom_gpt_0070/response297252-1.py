
import docx
import sys

# Set the default encoding (might be necessary for some environments)
reload(sys)
sys.setdefaultencoding('utf-8')

# Read the .docx file
document = docx.Document('sim_dir_administrativo.docx')

# Collect text from paragraphs without immediate encoding
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the document text, which is already a Unicode string
print docText

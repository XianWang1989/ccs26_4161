
import docx
import sys
import codecs

# Ensure the stdout can handle utf-8
reload(sys)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs and keep them in Unicode
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the Unicode string directly
print docText

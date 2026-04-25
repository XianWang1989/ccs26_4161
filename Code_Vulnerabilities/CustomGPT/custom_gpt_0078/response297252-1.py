
import docx
import sys
import codecs

# Ensure the terminal can handle UTF-8
if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

document = docx.Document('sim_dir_administrativo.docx')

# Collect text in Unicode
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print the text directly, now in Unicode
print(docText)

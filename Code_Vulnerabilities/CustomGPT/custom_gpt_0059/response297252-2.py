
import sys
import docx

# Ensure the console can handle UTF-8 output
reload(sys)
sys.stdout.encoding = 'utf-8'

document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)
print docText

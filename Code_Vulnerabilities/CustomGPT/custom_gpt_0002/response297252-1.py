
import docx
import sys

# Set the default encoding to utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

document = docx.Document('sim_dir_administrativo.docx')
docText = '\n\n'.join([
    paragraph.text for paragraph in document.paragraphs])  # Remove .encode('utf-8')

print(docText)  # No need to decode, just print directly

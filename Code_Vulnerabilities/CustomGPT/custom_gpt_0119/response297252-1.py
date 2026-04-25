
import docx

# Open the document as a Unicode string
document = docx.Document('sim_dir_administrativo.docx')
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Print output, encoding to UTF-8
print docText.encode('utf-8')

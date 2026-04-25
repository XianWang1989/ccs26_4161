
import docx

# Open the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect all paragraphs as a single Unicode string
docText = '\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# Since Python 2.7 can handle Unicode, you can directly print it
print docText.encode('utf-8')  # Encode for output if needed

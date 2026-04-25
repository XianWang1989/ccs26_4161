
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect paragraphs as a single Unicode string
docText = u'\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Now print it directly
print docText  # no need to decode, just print the Unicode string

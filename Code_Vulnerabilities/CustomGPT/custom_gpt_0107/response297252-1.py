
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect the text from paragraphs without immediate encoding
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Print the decoded text
# Use 'replace' to handle any problematic characters during encoding
print docText.encode('utf-8', 'replace')

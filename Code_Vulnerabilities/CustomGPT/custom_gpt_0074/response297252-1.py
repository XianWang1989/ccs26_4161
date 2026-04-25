
import docx

# Load the document
document = docx.Document('sim_dir_administrativo.docx')

# Collect all paragraphs and join them
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Output the text directly if you're just working within Python
print(docText)

# If you need to save or print out to a terminal that may not support UTF-8:
# You can encode to a specific encoding, like 'utf-8' or 'latin-1'
try:
    print(docText.encode('utf-8'))  # or 'latin-1', based on your needs
except UnicodeEncodeError as e:
    print("Encoding error:", e)

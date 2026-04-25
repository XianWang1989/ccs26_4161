
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Collect the text from the document paragraphs
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])  # Keep it as a Unicode string

# Now when printing, ensure it handles the encoding correctly
try:
    print(docText.encode('utf-8'))  # Encode when printing to make sure it handles special characters
except UnicodeEncodeError as e:
    print("Error encoding the text:", e)

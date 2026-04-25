
import docx

# Read the DOCX file
document = docx.Document('sim_dir_administrativo.docx')

# Join the paragraphs without encoding them yet
docText = u'\n\n'.join([
    paragraph.text for paragraph in document.paragraphs
])

# Print the text, ensuring the console can handle Unicode
try:
    print docText.encode('utf-8')
except UnicodeEncodeError as e:
    print "Encoding error:", e

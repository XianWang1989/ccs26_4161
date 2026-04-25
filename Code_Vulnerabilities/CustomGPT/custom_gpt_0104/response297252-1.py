
import docx

# Open the document
document = docx.Document('sim_dir_administrativo.docx')

# Join all paragraph texts using Unicode
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

# If you need to print it to the console, encode it safely
try:
    print docText.encode('utf-8')  # Encode for printing
except UnicodeEncodeError as e:
    print "Encoding error:", e

# If you want to decode it later, you can do it like this:
# For example, if you want to write it to a UTF-8 encoded file
with open('output.txt', 'wb') as f:
    f.write(docText.encode('utf-8'))  # Write the encoded text to a file


import docx

# Read the docx file
document = docx.Document('sim_dir_administrativo.docx')

# Collect the text from all paragraphs and join them
docText = '\n\n'.join(paragraph.text for paragraph in document.paragraphs)

# Ensure the output is properly encoded to UTF-8
try:
    print docText.encode('utf-8')  # Encode to UTF-8 for output
except UnicodeEncodeError as e:
    print("Encoding error: ", e)

# If you need to decode it later (though not typically necessary):
decoded_text = docText.decode("utf-8")
print(decoded_text)

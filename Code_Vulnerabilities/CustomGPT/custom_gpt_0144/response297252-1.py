# -*- coding: utf-8 -*-
import docx
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # Allows UTF-8 to be the default encoding

document = docx.Document('sim_dir_administrativo.docx')
docText = u'\n\n'.join([paragraph.text for paragraph in document.paragraphs])

print docText  # Now this should work without the encode-decode error

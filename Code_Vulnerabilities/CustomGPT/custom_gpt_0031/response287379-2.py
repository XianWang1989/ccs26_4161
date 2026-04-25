
import os
import sys

app_lib_path = os.path.join(os.getcwd(), 'appLib')
kb_gui_path = os.path.join(app_lib_path, 'KB-GUI')

sys.path.append(kb_gui_path)
sys.path.append(app_lib_path)

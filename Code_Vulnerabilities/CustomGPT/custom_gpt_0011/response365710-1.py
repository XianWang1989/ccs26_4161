
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.app import App
import cat_dict

Builder.load_string("""
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter


&lt;ListViewModal&gt;:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[(title, abbr) for title, abbr in root.categories.items()],
            args_converter=lambda row_index, rec: \
            {'text': rec[0], 'on_press': lambda instance: root.callback(rec[1]), 'size_hint_y': None, 'height': 25},
            cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = cat_dict.SECTION_DICT

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, abbreviation):
        print("Selected Abbreviation: " + abbreviation)

# Continuing with the rest of your code...

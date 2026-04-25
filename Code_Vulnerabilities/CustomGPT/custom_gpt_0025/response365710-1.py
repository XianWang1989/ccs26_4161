
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.app import App
import citylists
import cat_dict

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton

# Assuming cat_dict.SECTION_DICT is defined properly.
# cat_dict.py (only showing the relevant part)
SECTION_DICT = {
    "accounting+finance": "acc",
    "admin / office": "ofc",
    "arch / engineering": "egr",
    'art / media / design': 'med',
    'biotech / science': 'sci',
    'business / mgmt': 'bus',
    'customer management': 'csr',
    'education': 'edu',
}

Builder.load_string("""
<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[i for i in root.categories],
            args_converter=lambda row_index, rec: \
            {'text': rec, 'on_press': lambda x: root.callback(rec), 'size_hint_y': None, 'height': 25},
            cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = sorted(SECTION_DICT.keys())

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, title):
        abbreviation = SECTION_DICT[title]
        print("Abbreviation:", abbreviation)

class MainView(GridLayout):
    def __init__(self, **kwargs):
        kwargs['cols'] = 1
        super(MainView, self).__init__(**kwargs)

        listview_modal = ListViewModal()
        self.add_widget(listview_modal)

class MainScreen(Screen):
    pass

mainscreen = MainScreen()
mainlayout = MainView()
mainscreen.add_widget(mainlayout)

sm = ScreenManager()
sm.add_widget(mainscreen)

class CARApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    CARApp().run()

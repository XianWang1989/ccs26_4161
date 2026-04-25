
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton

# Sample dictionary for demonstration
SECTION_DICT = {
    "accounting+finance": "acc",
    "admin / office": "ofc",
    "arch / engineering": "egr",
    "art / media / design": "med",
    "biotech / science": "sci",
    "business / mgmt": "bus",
    "customer management": "csr",
    "education": "edu"
}

Builder.load_string("""
<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[i for i in root.categories],
            args_converter=lambda row_index, rec: \
            {'text': rec, 'on_press': lambda button: root.callback(button, root.section_dict[rec]), 'size_hint_y': None, 'height': 25},
            cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = sorted(SECTION_DICT.keys())
    section_dict = SECTION_DICT

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, instance, abbreviation):
        print("Button pressed:", instance.text)
        print("Abbreviation:", abbreviation)

class MainView(GridLayout):
    def __init__(self, **kwargs):
        kwargs['cols'] = 1
        super(MainView, self).__init__(**kwargs)

        listview_modal = ListViewModal()
        self.add_widget(listview_modal)

class MainScreen(Screen):
    pass

sm = ScreenManager()
mainscreen = MainScreen()
mainlayout = MainView()
mainscreen.add_widget(mainlayout)
sm.add_widget(mainscreen)

class CARApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    CARApp().run()

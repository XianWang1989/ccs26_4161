
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Example dictionary
cat_dict = {
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
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter

<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
                data=[i for i in root.categories],
                args_converter=lambda row_index, rec: \
                {'text': rec, 'on_press': lambda btn: root.callback(btn, cat_dict[rec]), 'size_hint_y': None, 'height': 25},
                cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = sorted(cat_dict.keys())  # Use keys for button titles

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, instance, abbreviation):
        print("Selected abbreviation: " + abbreviation)

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

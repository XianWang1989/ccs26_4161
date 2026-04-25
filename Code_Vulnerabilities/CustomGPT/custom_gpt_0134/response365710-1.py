
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

import cat_dict  # Assuming this contains the dictionary

Builder.load_string("""
<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[i for i in root.categories],
            args_converter=lambda row_index, rec: {
                'text': rec, 
                'on_press': lambda instance: root.callback(rec),  # Pass title to callback
                'size_hint_y': None, 
                'height': 25
            },
            cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT)

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, title):
        abbreviation = cat_dict.SECTION_DICT[title]  # Get abbreviation
        print(f"Title: {title}, Abbreviation: {abbreviation}")

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

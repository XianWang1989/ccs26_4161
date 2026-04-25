
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.app import App
import cat_dict

Builder.load_string("""
#:import ListItemButton kivy.uix.listview.ListItemButton
#:import ListAdapter kivy.adapters.listadapter.ListAdapter

<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
            data=[(key, value) for key, value in root.categories.items()],
            args_converter=lambda row_index, rec: \
            {'text': rec[0], 'on_press': lambda x: root.callback(rec[1]), 'size_hint_y': None, 'height': 25},
            cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = cat_dict.SECTION_DICT

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, abbreviation):
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

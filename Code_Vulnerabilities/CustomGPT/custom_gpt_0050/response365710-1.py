
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Assuming cat_dict is already imported
import cat_dict

Builder.load_string("""
<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
                data=[i for i in root.categories],
                args_converter=lambda row_index, rec: \
                {'text': rec, 'on_press': lambda instance, rec=rec: root.callback(instance, rec), 
                 'size_hint_y': None, 'height': 25},
                cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT.keys())

    def callback(self, instance, title):
        abbreviation = cat_dict.SECTION_DICT[title]
        print("Button Pressed: Title =", title, ", Abbreviation =", abbreviation)

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

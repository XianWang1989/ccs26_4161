
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.app import App
import cat_dict  # Ensure cat_dict is correctly named

Builder.load_string("""
<ListViewModal>:
    ListView:
        size_hint: .8, .8
        adapter:
            ListAdapter(
                data=[(title, abbr) for title, abbr in root.categories.items()],
                args_converter=lambda row_index, rec: \
                {'text': rec[0], 'abbr': rec[1], 'on_press': root.callback, 'size_hint_y': None, 'height': 25},
                cls=ListItemButton)

""")

class ListViewModal(ModalView):
    categories = sorted(cat_dict.EECTION_DICT.items())

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, instance):
        abbr = instance.abbr  # Get the abbreviation from the instance
        print("Abbreviation:", abbr)  # Print the abbreviation

class MainView(GridLayout):
    def __init__(self, **kwargs):
        kwargs['cols'] = 1
        super(MainView, self).__init__(**kwargs)

        listview_modal = ListViewModal()
        self.add_widget(listview_modal)

class MainScreen(Screen):
    pass

# Setting up ScreenManager
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

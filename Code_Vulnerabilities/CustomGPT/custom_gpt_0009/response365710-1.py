
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
            data=[{'title': title, 'abbreviation': cat_dict.SECTION_DICT[title]} for title in root.categories],
            args_converter=lambda row_index, rec: \
            {'text': rec['title'], 'on_press': root.callback, 'size_hint_y': None, 'height': 25, 'abbreviation': rec['abbreviation']},
            cls=ListItemButton)
""")

class ListViewModal(ModalView):
    categories = sorted(cat_dict.SECTION_DICT)

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)

    def callback(self, instance):
        # Access the abbreviation from the button's properties
        abbreviation = instance.abbreviation
        print("Clicked abbreviation: " + abbreviation)

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
